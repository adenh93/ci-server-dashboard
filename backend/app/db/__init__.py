import databases
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from starlette.requests import Request
from .. import config
from fastapi import FastAPI

db = databases.Database(config.DATABASE_URI)

engine = sqlalchemy.create_engine(
    config.DATABASE_URI, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db(request: Request):
    return request.state.db
