from passlib.context import CryptContext
from sqlalchemy.orm import Session
from ..db.services import users_db, user_logins_db
from ..models.auth import (
    UserRegistrationRequest
)

crypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


async def insert_user(request: UserRegistrationRequest):
    request.password = crypt_context.hash(request.password)
    user_id = await users_db.insert_user(request)
    return user_id


async def insert_user_login(user_id: int):
    login_id = await user_logins_db.insert_user_login(user_id)
    return login_id
