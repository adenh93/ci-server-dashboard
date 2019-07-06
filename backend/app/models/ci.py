from pydantic import BaseModel
from typing import List
from .enums import CIService


class UserApiKeyRequest(BaseModel):
    user_id: int
    service: str
    key: str
