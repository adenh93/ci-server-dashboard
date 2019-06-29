from sqlalchemy import Column, DateTime, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    name = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    created_date = Column(DateTime, nullable=False, default=datetime.now())


class UserLogin(Base):
    __tablename__ = 'user_login'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    login_date = Column(DateTime, nullable=False, default=datetime.now())


class UserApiKey(Base):
    __tablename__ = 'user_api_key'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    service = Column(String(100), nullable=False)
    key = Column(String(255), nullable=False)
