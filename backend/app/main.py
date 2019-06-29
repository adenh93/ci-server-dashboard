from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response
from .api import router as api_router
from .config import DATABASE_URI
from .db import db, SessionLocal


app = FastAPI()
app.include_router(api_router, prefix="/api")


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()
