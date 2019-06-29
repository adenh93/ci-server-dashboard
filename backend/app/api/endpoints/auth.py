from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette.responses import JSONResponse
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_201_CREATED
from sqlalchemy.orm import Session
from datetime import timedelta
from ...models.auth import Token, UserRegistrationRequest
from ...services.auth import authenticate_user, create_access_token, insert_user
from ...config import ACCESS_TOKEN_EXPIRY_MINUTES
from ...db import get_db

router = APIRouter()


@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = await authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRY_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/register", status_code=HTTP_201_CREATED)
async def register(request: UserRegistrationRequest, db: Session = Depends(get_db)):
    user_id = await insert_user(db, request)
    return {'id': user_id}
