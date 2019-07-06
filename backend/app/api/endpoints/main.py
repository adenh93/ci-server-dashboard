from fastapi import APIRouter
from starlette.responses import JSONResponse
from ...models.main import Settings
from ...utils.auth_utils import get_current_user

router = APIRouter()


@router.get("/settings", response_model=Settings)
async def get_settings():
    settings = Settings()
    settings.user = await get_current_user()
    return settings
