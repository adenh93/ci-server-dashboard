from pydantic import BaseModel
from typing import List
from .enums import CIService


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str


class ApiKey(BaseModel):
    service: CIService
    key: str


class UserRegistrationRequest(BaseModel):
    username: str
    email: str
    password: str
    name: str


class UserDetails(BaseModel):
    id: int
    username: str
    email: str
    display_name: str
    keys: List[ApiKey] = []