from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import user_routes
from app.database import init_db

app = FastAPI(title="API Backend - FastAPI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()

app.include_router(user_routes.router, prefix="/users", tags=["Users"])

@app.get("/")
def home():
    return {"message": "API online 🚀"}
