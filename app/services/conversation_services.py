from sqlalchemy.orm import Session
from app.models import conversation_model
from app.schemas import conversation_schemas
from typing import List, Optional

def create_conversation(db: Session, conversation_data: conversation_schemas.ConversationCreate):
    """Cria uma nova conversa"""
    conversation = conversation_model.Conversation(
        title=conversation_data.title,
        user_id=conversation_data.user_id
    )
    db.add(conversation)
    db.commit()
    db.refresh(conversation)
    return conversation

def get_conversation(db: Session, conversation_id: int):
    """Busca uma conversa por ID"""
    return db.query(conversation_model.Conversation).filter(
        conversation_model.Conversation.id == conversation_id
    ).first()

def list_conversations(db: Session, user_id: Optional[int] = None, limit: int = 50):
    """Lista conversas (opcionalmente filtra por usuário)"""
    query = db.query(conversation_model.Conversation)
    
    if user_id:
        query = query.filter(conversation_model.Conversation.user_id == user_id)
    
    conversations = query.order_by(
        conversation_model.Conversation.updated_at.desc()
    ).limit(limit).all()
    
    # Adiciona contagem de mensagens
    result = []
    for conv in conversations:
        result.append({
            "id": conv.id,
            "title": conv.title,
            "created_at": conv.created_at,
            "updated_at": conv.updated_at,
            "message_count": len(conv.messages)
        })
    
    return result

def update_conversation(db: Session, conversation_id: int, update_data: conversation_schemas.ConversationUpdate):
    """Atualiza uma conversa"""
    conversation = get_conversation(db, conversation_id)
    if not conversation:
        return None
    
    if update_data.title:
        conversation.title = update_data.title
    
    db.commit()
    db.refresh(conversation)
    return conversation

def delete_conversation(db: Session, conversation_id: int):
    """Deleta uma conversa e todas as suas mensagens"""
    conversation = get_conversation(db, conversation_id)
    if not conversation:
        return False
    
    db.delete(conversation)
    db.commit()
    return True

def add_message(
    db: Session, 
    conversation_id: int, 
    message_data: conversation_schemas.MessageCreate
):
    """Adiciona uma mensagem à conversa"""
    message = conversation_model.Message(
        conversation_id=conversation_id,
        role=message_data.role,
        content=message_data.content,
        model=message_data.model,
        tokens_used=message_data.tokens_used,
        input_tokens=message_data.input_tokens,
        output_tokens=message_data.output_tokens
    )
    db.add(message)
    db.commit()
    db.refresh(message)
    
    # Atualiza o timestamp da conversa
    conversation = get_conversation(db, conversation_id)
    if conversation:
        from datetime import datetime
        conversation.updated_at = datetime.utcnow()
        db.commit()
    
    return message

def get_conversation_history(db: Session, conversation_id: int):
    """Retorna o histórico de mensagens de uma conversa"""
    messages = db.query(conversation_model.Message).filter(
        conversation_model.Message.conversation_id == conversation_id
    ).order_by(conversation_model.Message.created_at).all()
    
    return [{"role": msg.role, "content": msg.content} for msg in messages]