from passlib.context import CryptContext
# Manages hashing algorithms.
from datetime import datetime, timedelta
from jose import jwt
from app.core.config import (
    SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES
)
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer


pwd_context = CryptContext(
    schemes=["bcrypt"],
    # Very popular secure hashing algorithm.

    deprecated="auto"
)

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(
    plain_password,
    hashed_password
):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )

def create_access_token(data: dict):

    # Copy user data
    to_encode = data.copy()

    # Set token expiry time
    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    # Add expiry into token payload
    to_encode.update({
        "exp": expire
    })

    # Generate JWT token
    # Creates secure signed token.
    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt


def verify_access_token(token: str):

    try:

        # Decode JWT token
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        # Extract user email
        email = payload.get("sub")

        if email is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return email

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Token is invalid or expired"
        )
    
def get_current_user(
    token: str = Depends(oauth2_scheme)
):

    # Verify token
    email = verify_access_token(token)

    return email

