from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.core.security import (
    verify_password,
    create_access_token
)

from app.schemas.user_schema import (
    UserCreate,
    UserLogin
)

from app.database.session import get_db
from app.models.user import User
from app.core.security import hash_password
from app.core.security import get_current_user
from app.core.security import verify_access_token


from jose import JWTError, jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()


@router.post("/users")
async def create_user(
    # data vvalidation from schemas using pyndantic
    user: UserCreate,

    # db session fromm session for dependency injection   
    db: Session = Depends(get_db)
):
    new_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password)
    )

# Adds object to DB session.
    db.add(new_user)

# Actually saves data to PostgreSQL
    db.commit()

# Refreshes object from DB.
    db.refresh(new_user)

    return {
        "message": "User created successfully"
    }



@router.post("/login")
async def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    # Find user by email
    existing_user = db.execute(
        select(User).where(
            User.email == user.email
        )
    ).scalar_one_or_none()

    # Check if user exists
    if not existing_user:
        return {
            "message": "Invalid email"
        }

    # Verify password
    valid_password = verify_password(
        user.password,
        existing_user.password
    )

    if not valid_password:
        return {
            "message": "Invalid password"
        }

    # Create JWT token
    access_token = create_access_token(
        data={
            "sub": existing_user.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.get("/profile")
async def profile(
    token: str
):

    email = verify_access_token(token)

    return {
        "message": "Protected route accessed",
        "user": email
    }