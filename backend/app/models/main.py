from pydantic import BaseModel
from typing import List
from .auth import UserDetails


class Settings(BaseModel):
    user: UserDetails
