from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from ...utils.auth_utils import get_current_user
from ...services.ci_service import insert_api_key, get_builds
from ...models.ci import UserApiKeyRequest

router = APIRouter()


@router.post("/service", status_code=HTTP_201_CREATED)
async def add_new_api_key(request: UserApiKeyRequest):
    current_user = await get_current_user()
    user_has_service = next((key for key in current_user.keys
                            if key.service == request.service), None)
    if user_has_service:
        raise HTTPException(
            code=HTTP_400_BAD_REQUEST,
            detail="An API key for this service already exists."
        )
    request.user_id = current_user.id
    await insert_api_key(request)
