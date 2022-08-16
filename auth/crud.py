from typing import Union

from sqlalchemy.orm import Session

from auth.models import User
from auth.schemas import UserFormDataSchema, UserSchemaOrm
from auth.utils import get_password_hash


def get_user(db: Session, username):
    user = db.query(User).filter_by(username=username).first()
    if user:
        return user


def get_all_users(db: Session):
    return db.query(User).all()


def create_user(db: Session, data: UserFormDataSchema):
    user = User(username=data.username, password_hash=get_password_hash(data.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
