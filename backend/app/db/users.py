from .model import User
from sqlalchemy.orm import Session


def get_user_by_username(db: Session, username: str):
    user = db.query(User).filter(User.username == username)
    return user.first()


def get_user_by_id(db: Session, id: int):
    user = db.query(User).filter(User.id == id)
    return user.first()


def get_users(db: Session):
    return db.query(User)


def insert_user(db: Session, user: User):
    db.add(user)
    db.commit()
    return user.id
