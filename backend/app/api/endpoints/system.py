from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse
from ...models.main import Settings
from ...utils.auth_utils import get_current_user
from ...models.auth import UserDetails

router = APIRouter()


@router.get("/settings", tags=['system'], response_model=Settings)
async def get_settings():
    """
    Returns the system settings to be used on the frontend.
    """
    return None
