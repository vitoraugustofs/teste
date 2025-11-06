from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.routes import user_routes, ai_routes, conversation_routes
from app.database import init_db
import os

app = FastAPI(
    title="API Backend - FastAPI + Claude AI",
    description="Backend com autenticação, Claude AI e sistema de conversas",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializa o banco de dados
init_db()

# Rotas da API
app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(ai_routes.router, prefix="/ai", tags=["Claude AI"])
app.include_router(conversation_routes.router, prefix="/conversations", tags=["Conversations"])

@app.get("/")
def home():
    return {
        "message": "API online 🚀",
        "services": ["Users", "Claude AI", "Conversations"],
        "docs": "/docs",
        "chat_interface": "/chat"
    }

# Serve a interface web (opcional - crie uma pasta 'static' e coloque o HTML lá)
# Se você quiser servir o HTML diretamente:
@app.get("/chat")
def chat_interface():
    """Serve a interface de chat"""
    # Você pode criar um arquivo static/chat.html com o HTML fornecido
    return FileResponse("static/chat.html")
