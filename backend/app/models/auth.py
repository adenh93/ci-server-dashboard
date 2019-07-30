from pydantic import BaseModel
from typing import List
from .enums import CIService


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str


class ApiKey(BaseModel):
    service: str
    key: str


class UserLoginRequest(BaseModel):
    username: str
    password: str


class UserRegistrationRequest(BaseModel):
    username: str
    email: str
    password: str
    name: str


class UserDetails(BaseModel):
    id: int
    username: str
    email: str
    name: str
    keys: List[ApiKey] = []
