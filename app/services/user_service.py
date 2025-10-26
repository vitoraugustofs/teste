from sqlalchemy.orm import Session
from app import models, schemas
from app.utils.security import hash_password

def create_user(db: Session, user_data: schemas.UserCreate):
    hashed_pw = hash_password(user_data.password)
    new_user = models.user_model.User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hashed_pw,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def list_users(db: Session):
    return db.query(models.user_model.User).all()
