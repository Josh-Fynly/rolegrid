from sqlalchemy.orm import Session

from app.models.user import User
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)


def register_user(db: Session, email: str, password: str, full_name: str):
    existing = db.query(User).filter(User.email == email).first()

    if existing:
        return None

    user = User(
        email=email,
        password_hash=hash_password(password),
        full_name=full_name
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()

    if not user:
        return None

    if not verify_password(password, user.password_hash):
        return None

    token = create_access_token(
        data={
            "sub": str(user.id),
            "email": user.email
        }
    )

    return token


def get_user_by_id(db: Session, user_id: str):
    return db.query(User).filter(User.id == user_id).first()
