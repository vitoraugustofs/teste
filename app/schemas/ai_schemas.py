from pydantic import BaseModel, Field
from typing import Optional, List

class ChatRequest(BaseModel):
    """Schema para requisição de chat"""
    message: str = Field(..., description="Mensagem para enviar ao Claude")
    system_prompt: Optional[str] = Field(None, description="Instrução de sistema para o Claude")
    model: Optional[str] = Field("claude-3-5-sonnet-20241022", description="Modelo Claude a usar")
    max_tokens: Optional[int] = Field(1024, ge=1, le=4096, description="Máximo de tokens na resposta")
    temperature: Optional[float] = Field(1.0, ge=0, le=1, description="Temperatura (criatividade)")

class ChatResponse(BaseModel):
    """Schema para resposta do chat"""
    success: bool
    response: str
    tokens_used: int
    input_tokens: int
    output_tokens: int
    model: str

class ConversationMessage(BaseModel):
    """Schema para uma mensagem na conversa"""
    role: str = Field(..., description="'user' ou 'assistant'")
    content: str = Field(..., description="Conteúdo da mensagem")

class ChatWithContextRequest(BaseModel):
    """Schema para chat com contexto/histórico"""
    message: str
    conversation_history: List[ConversationMessage] = Field(default=[], description="Histórico da conversa")
    system_prompt: Optional[str] = None
    model: Optional[str] = "claude-3-5-sonnet-20241022"

class ChatWithContextResponse(BaseModel):
    """Schema para resposta do chat com contexto"""
    success: bool
    response: str
    tokens_used: int
    input_tokens: int
    output_tokens: int

class ErrorResponse(BaseModel):
    """Schema para respostas de erro"""
    success: bool = False
    error: str

class ModelInfo(BaseModel):
    """Schema para informações de um modelo"""
    id: str
    name: str
    description: str

class ModelsResponse(BaseModel):
    """Schema para lista de modelos disponíveis"""
    models: List[ModelInfo]