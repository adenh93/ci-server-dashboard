import jwt
import functools
from jwt import PyJWTError
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from ..config import SECRET_KEY, ENCODE_ALGORITHM
from ..db import users_db, api_keys_db
from ..models.auth import (
    TokenData, UserRegistrationRequest, UserDetails, ApiKey
)

crypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


async def logged_in():
    def real_decorator(f):
        def wraps(*args, **kwargs):
            user = get_current_user()
            if user:
                return f(*args, **kwargs)
            return HTTPException(
                status_code=HTTP_403_FORBIDDEN
            )
        return functools.update_wrapper(wraps, f)
    return real_decorator


async def authenticate_user(username: str, password: str):
    user = await users_db.get_user_by_username(username)
    if not user:
        return False
    if not crypt_context.verify(password, user.password):
        return False
    return user


async def create_access_token(*, data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expires = datetime.utcnow() + expires_delta
    else:
        expires = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expires})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ENCODE_ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
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
    user = await users_db.get_user_by_username(token_data.username)
    if user is None:
        raise invalid_credentials

    user_keys = await api_keys_db.get_api_keys_for_user(user.id)
    user_details = UserDetails(**user)
    user_details.keys = [ApiKey(**key) for key in user_keys]
    return user_details
