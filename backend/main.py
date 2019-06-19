import databases
import config
from fastapi import FastAPI

database = databases.Database(config.DATABASE_URI)
app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
