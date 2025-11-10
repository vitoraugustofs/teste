from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class MessageBase(BaseModel):
    role: str
    content: str

class MessageCreate(MessageBase):
    model: Optional[str] = None
    tokens_used: Optional[int] = 0
    input_tokens: Optional[int] = 0
    output_tokens: Optional[int] = 0

class MessageResponse(MessageBase):
    id: int
    conversation_id: int
    model: Optional[str]
    tokens_used: int
    input_tokens: int
    output_tokens: int
    created_at: datetime

    class Config:
        from_attributes = True

class ConversationCreate(BaseModel):
    title: Optional[str] = "Nova Conversa"
    user_id: Optional[int] = None

class ConversationResponse(BaseModel):
    id: int
    title: str
    user_id: Optional[int]
    created_at: datetime
    updated_at: datetime
    messages: List[MessageResponse] = []

    class Config:
        from_attributes = True

class ConversationListResponse(BaseModel):
    id: int
    title: str
    created_at: datetime
    updated_at: datetime
    message_count: int

class ConversationUpdate(BaseModel):
    title: Optional[str] = None