import databases
import config
from fastapi import FastAPI
from api import router as api_router

database = databases.Database(config.DATABASE_URI)
app = FastAPI()

app.include_router(api_router, prefix="/api")


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
