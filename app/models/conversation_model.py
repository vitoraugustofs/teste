from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Conversation(Base):
    """Representa uma conversa completa"""
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    title = Column(String(200), default="Nova Conversa")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relacionamento com mensagens
    messages = relationship("Message", back_populates="conversation", cascade="all, delete-orphan")
    
    # Relacionamento com usuário (opcional)
    user = relationship("User", back_populates="conversations")


class Message(Base):
    """Representa uma mensagem individual na conversa"""
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey("conversations.id"))
    role = Column(String(20))  # 'user' ou 'assistant'
    content = Column(Text)
    model = Column(String(100), nullable=True)  # Modelo usado (ex: claude-3-5-sonnet)
    tokens_used = Column(Integer, default=0)
    input_tokens = Column(Integer, default=0)
    output_tokens = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relacionamento com conversa
    conversation = relationship("Conversation", back_populates="messages")