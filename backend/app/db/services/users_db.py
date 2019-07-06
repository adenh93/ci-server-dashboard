from datetime import datetime
from ..tables import users
from ...models.auth import UserRegistrationRequest
from .. import db


async def get_user_by_username(username: str):
    query = users.select().where(users.c.username == username)
    return await db.fetch_one(query)


async def get_user_by_id(id: int):
    query = users.select().where(users.c.id == id)
    return await db.fetch_one(query)


async def get_users():
    query = users.select()
    return await db.fetch_all(query)


async def insert_user(user: UserRegistrationRequest):
    query = users.insert().values(
        username=user.username,
        email=user.email,
        name=user.name,
        password=user.password,
        created_date=datetime.now()
    )
    return await db.execute(query)
