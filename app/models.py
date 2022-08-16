from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class TodoList(Base):
    __tablename__ = 'app_todo_list'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, default='')
    done = Column(Boolean, nullable=False, default=False)
    owner_id = Column(Integer, ForeignKey('auth_user.id', ondelete='CASCADE'), nullable=False)

    items = relationship("TodoItem", back_populates="list", cascade="all, delete")
    owner = relationship("User", back_populates="lists")


class TodoItem(Base):
    __tablename__ = 'app_todo_item'
    id = Column(Integer, primary_key=True)
    body = Column(String, nullable=False)
    done = Column(Boolean, nullable=False, default=False)
    list_id = Column(Integer, ForeignKey('app_todo_list.id', ondelete='CASCADE'))

    list = relationship("TodoList", back_populates="items")
