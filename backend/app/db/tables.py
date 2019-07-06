from sqlalchemy import (
    Table, Column, DateTime, String, Integer, ForeignKey, MetaData
)
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()


users = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String(100), nullable=False, unique=True),
    Column('email', String(255), nullable=False, unique=True),
    Column('name', String(255), nullable=False),
    Column('password', String(255), nullable=False),
    Column('created_date', DateTime, nullable=False)
)


user_logins = Table(
    'user_login',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('login_date', DateTime, nullable=False)
)


user_api_keys = Table(
    'user_api_key',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('service', String(100), nullable=False),
    Column('key', String(255), nullable=False)
)
