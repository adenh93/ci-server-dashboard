from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette.responses import JSONResponse
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_201_CREATED
from sqlalchemy.orm import Session
from datetime import timedelta
from ...models.auth import Token, UserRegistrationRequest
from ...utils.auth_utils import authenticate_user, create_access_token
from ...services.auth_service import insert_user, insert_user_login
from ...config import ACCESS_TOKEN_EXPIRY_MINUTES

router = APIRouter()


@router.post("/login", tags=['auth'], response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Accepts a username and password submitted via form-data, and attempts to
    authenticate the user. Returns a temporary access token if authentication
    is successful.
    """
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRY_MINUTES)
    access_token = await create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    await insert_user_login(user.id)
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/register", tags=['auth'], status_code=HTTP_201_CREATED)
async def register(request: UserRegistrationRequest):
    """
    Allows the user to register a new account in the system. Accepts JSON
    via the HTTP request body.
    """
    user_id = await insert_user(request)
    return {'id': user_id}
