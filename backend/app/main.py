import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response
from .api import router as api_router
from .config import DATABASE_URI
from .db import db

app = FastAPI(title='CI Dashboard')
app.include_router(api_router, prefix="/api")


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()
