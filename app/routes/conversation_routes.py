from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import conversation_schemas, ai_schemas
from app.services import conversation_service, ai_service
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=conversation_schemas.ConversationResponse)
def create_conversation(
    conversation: conversation_schemas.ConversationCreate,
    db: Session = Depends(get_db)
):
    """Cria uma nova conversa"""
    return conversation_service.create_conversation(db, conversation)

@router.get("/", response_model=List[conversation_schemas.ConversationListResponse])
def list_conversations(
    user_id: int = None,
    limit: int = 50,
    db: Session = Depends(get_db)
):
    """Lista todas as conversas"""
    return conversation_service.list_conversations(db, user_id, limit)

@router.get("/{conversation_id}", response_model=conversation_schemas.ConversationResponse)
def get_conversation(conversation_id: int, db: Session = Depends(get_db)):
    """Busca uma conversa específica com todas as mensagens"""
    conversation = conversation_service.get_conversation(db, conversation_id)
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversa não encontrada")
    return conversation

@router.patch("/{conversation_id}", response_model=conversation_schemas.ConversationResponse)
def update_conversation(
    conversation_id: int,
    update_data: conversation_schemas.ConversationUpdate,
    db: Session = Depends(get_db)
):
    """Atualiza o título de uma conversa"""
    conversation = conversation_service.update_conversation(db, conversation_id, update_data)
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversa não encontrada")
    return conversation

@router.delete("/{conversation_id}")
def delete_conversation(conversation_id: int, db: Session = Depends(get_db)):
    """Deleta uma conversa"""
    success = conversation_service.delete_conversation(db, conversation_id)
    if not success:
        raise HTTPException(status_code=404, detail="Conversa não encontrada")
    return {"message": "Conversa deletada com sucesso"}

@router.post("/{conversation_id}/message", response_model=ai_schemas.ChatResponse)
def send_message(
    conversation_id: int,
    request: ai_schemas.ChatRequest,
    db: Session = Depends(get_db)
):
    """
    Envia uma mensagem em uma conversa existente e salva no banco.
    O Claude responderá usando o contexto completo da conversa.
    """
    # Verifica se a conversa existe
    conversation = conversation_service.get_conversation(db, conversation_id)
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversa não encontrada")
    
    # Salva a mensagem do usuário
    user_message = conversation_service.add_message(
        db,
        conversation_id,
        conversation_schemas.MessageCreate(
            role="user",
            content=request.message
        )
    )
    
    # Busca histórico da conversa
    history = conversation_service.get_conversation_history(db, conversation_id)
    
    # Remove a última mensagem (que acabamos de adicionar) do histórico
    # pois vamos enviá-la separadamente
    history = history[:-1]
    
    try:
        # Chama o Claude com o contexto
        result = ai_service.chat_with_context(
            message=request.message,
            conversation_history=history,
            system_prompt=request.system_prompt,
            model=request.model
        )
        
        # Salva a resposta do Claude
        ai_message = conversation_service.add_message(
            db,
            conversation_id,
            conversation_schemas.MessageCreate(
                role="assistant",
                content=result['response'],
                model=request.model,
                tokens_used=result['tokens_used'],
                input_tokens=result['input_tokens'],
                output_tokens=result['output_tokens']
            )
        )
        
        return ai_schemas.ChatResponse(
            success=True,
            response=result['response'],
            tokens_used=result['tokens_used'],
            input_tokens=result['input_tokens'],
            output_tokens=result['output_tokens'],
            model=request.model
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao processar mensagem: {str(e)}"
        )