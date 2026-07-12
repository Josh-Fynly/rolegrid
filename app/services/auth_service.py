from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)

from app.models.user import User


def register_user(
    db: Session,
    email: str,
    password: str,
    full_name: str,
):
    """
    Register a new user.

    Returns:
        User | None
    """

    existing_user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if existing_user:
        return None

    new_user = User(
        email=email,
        password_hash=hash_password(password),
        full_name=full_name,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def authenticate_user(
    db: Session,
    email: str,
    password: str,
):
    """
    Authenticate a user.

    Returns:
        JWT token string | None
    """

    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if not user:
        return None

    if not verify_password(
        password,
        user.password_hash,
    ):
        return None

    return create_access_token(
        data={
            "sub": str(user.id),
            "email": user.email,
        }
    )
