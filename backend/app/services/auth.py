import jwt
from jwt import PyJWTError
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from starlette.status import HTTP_401_UNAUTHORIZED
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from ..config import SECRET_KEY, ENCODE_ALGORITHM
from ..db import users
from ..db.model import User
from ..models.auth import TokenData, UserRegistrationRequest

crypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


async def insert_user(db: Session, request: UserRegistrationRequest):
    user = User(**request.dict())
    user.password = crypt_context.hash(request.password)
    user_id = users.insert_user(db, user)
    return user_id


async def authenticate_user(db: Session, username: str, password: str):
    user = users.get_user_by_username(db, username)
    if not user:
        return False
    if not crypt_context.verify(password, user.password):
        return False
    return user


def create_access_token(*, data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expires = datetime.utcnow() + expires_delta
    else:
        expires = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expires})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ENCODE_ALGORITHM)
    return encoded_jwt


async def get_current_user(db: Session, token: str = Depends(oauth2_scheme)):
    invalid_credentials = HTTPException(
        status_code=HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials"
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ENCODE_ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise invalid_credentials
        token_data = TokenData(username=username)
    except PyJWTError:
        raise invalid_credentials
    user = users.get_user_by_username(db, token_data.username)
    if user is None:
        raise invalid_credentials
    return user
