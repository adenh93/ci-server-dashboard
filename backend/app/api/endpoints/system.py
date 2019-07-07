from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse
from ...models.main import Settings
from ...utils.auth_utils import get_current_user, oauth2_scheme

router = APIRouter()


@router.get("/settings", tags=['system'], response_model=Settings)
async def get_settings(token: str = Depends(oauth2_scheme)):
    """
    Returns the system settings to be used on the frontend, including
    information about the current user.
    """
    settings = Settings()
    settings.user = await get_current_user()
    return settings
