from sqlalchemy.orm import Session
from ..models.ci import UserApiKeyRequest
from ..db.services import api_keys_db
from ..utils.crypto_utils import encrypt_key, decrypt_key


async def insert_api_key(request: UserApiKeyRequest):
    request.key = encrypt_key(request.key)
    id = await api_keys_db.insert_api_key(request)
    return id
