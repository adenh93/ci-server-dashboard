from sqlalchemy import Column, DateTime, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_date = Column(DateTime, nullable=False)


class UserLogin(Base):
    __tablename__ = 'user_login'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    login_date = Column(DateTime, nullable=False)


class UserApiKey(Base):
    __tablename__ = 'user_api_key'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    service = Column(String(100), nullable=False)
    key = Column(String(255), nullable=False)
