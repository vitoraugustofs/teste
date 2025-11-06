# app/routes/ai_routes.py
from fastapi import APIRouter, HTTPException
from app.schemas import ai_schemas
from app.services import ai_service

router = APIRouter()

@router.post("/chat", response_model=ai_schemas.ChatResponse)
def chat(request: ai_schemas.ChatRequest):
    """
    Conversa com o Claude AI (sem salvar no banco)
    
    **Exemplo de request:**
    ```json
    {
        "message": "Olá Claude, como você está?",
        "system_prompt": "Você é um assistente prestativo",
        "model": "claude-3-5-sonnet-20241022",
        "max_tokens": 1024,
        "temperature": 1.0
    }
    ```
    
    **Modelos disponíveis:**
    - `claude-3-5-sonnet-20241022` (Recomendado - mais inteligente)
    - `claude-3-5-haiku-20241022` (Mais rápido e econômico)
    - `claude-3-opus-20240229` (Alta performance)
    """
    try:
        if not request.message.strip():
            raise HTTPException(
                status_code=400,
                detail="Mensagem não pode estar vazia"
            )
        
        result = ai_service.chat_with_ai(
            message=request.message,
            system_prompt=request.system_prompt,
            model=request.model,
            max_tokens=request.max_tokens,
            temperature=request.temperature
        )
        
        return ai_schemas.ChatResponse(
            success=True,
            response=result['response'],
            tokens_used=result['tokens_used'],
            input_tokens=result['input_tokens'],
            output_tokens=result['output_tokens'],
            model=result['model']
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao processar mensagem: {str(e)}"
        )

@router.post("/chat/context", response_model=ai_schemas.ChatWithContextResponse)
def chat_with_context(request: ai_schemas.ChatWithContextRequest):
    """
    Chat com Claude mantendo contexto da conversa (sem salvar no banco)
    
    **Exemplo de request:**
    ```json
    {
        "message": "E sobre Python?",
        "conversation_history": [
            {"role": "user", "content": "Fale sobre programação"},
            {"role": "assistant", "content": "Programação é..."}
        ],
        "model": "claude-3-5-sonnet-20241022"
    }
    ```
    
    **Importante:** O histórico deve alternar entre 'user' e 'assistant'.
    A primeira mensagem deve ser sempre do 'user'.
    """
    try:
        if not request.message.strip():
            raise HTTPException(
                status_code=400,
                detail="Mensagem não pode estar vazia"
            )
        
        # Converte Pydantic models para dicts
        history = [{"role": msg.role, "content": msg.content} 
                   for msg in request.conversation_history]
        
        result = ai_service.chat_with_context(
            message=request.message,
            conversation_history=history,
            system_prompt=request.system_prompt,
            model=request.model
        )
        
        return ai_schemas.ChatWithContextResponse(
            success=True,
            response=result['response'],
            tokens_used=result['tokens_used'],
            input_tokens=result['input_tokens'],
            output_tokens=result['output_tokens']
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao processar mensagem: {str(e)}"
        )

@router.post("/analyze")
def analyze_query(request: ai_schemas.ChatRequest):
    """
    Analisa a intenção de uma mensagem usando Claude
    
    **Exemplo:**
    ```json
    {
        "message": "Estou com um problema no sistema"
    }
    ```
    
    **Retorna:**
    - intent: tipo de mensagem (pergunta, ajuda, reclamação, etc)
    - confidence: nível de confiança da análise (0-1)
    """
    try:
        if not request.message.strip():
            raise HTTPException(
                status_code=400,
                detail="Mensagem não pode estar vazia"
            )
        
        result = ai_service.analyze_user_query(request.message)
        return {
            "success": True,
            "intent": result.get('intent', 'unknown'),
            "confidence": result.get('confidence', 0.0),
            "message": request.message
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao analisar mensagem: {str(e)}"
        )

@router.get("/models", response_model=ai_schemas.ModelsResponse)
def list_models():
    """
    Lista todos os modelos Claude disponíveis
    """
    models = ai_service.get_available_models()
    return ai_schemas.ModelsResponse(models=models)

@router.get("/health")
def health_check():
    """
    Verifica se a integração com Claude está configurada
    """
    import os
    
    has_key = bool(os.getenv('ANTHROPIC_API_KEY'))
    
    return {
        "status": "online" if has_key else "no_api_key",
        "service": "Anthropic Claude",
        "message": "Claude configurado ✅" if has_key else "⚠️ Configure ANTHROPIC_API_KEY no arquivo .env"
    }