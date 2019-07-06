from .tables import user_api_keys
from ..models.ci import UserApiKeyRequest
from . import db


async def get_api_keys_for_user(user_id: int):
    query = user_api_keys.select()
    return await db.fetch_all(query)


async def insert_api_key(api_key: UserApiKeyRequest):
    query = user_api_keys.insert().values(
        user_id=api_key.user_id,
        service=api_key.service,
        key=api_key.key
    )
    return await db.execute(query)
