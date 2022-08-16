from sqlalchemy.orm import Session

from app.models import TodoItem
from app.models import TodoList


def get_lists_for_user(db: Session, user_id):
    return db.query(TodoList).filter_by(owner_id=user_id).all()


def get_list_by_id(db: Session, list_id) -> TodoList:
    return db.query(TodoList).filter_by(id=list_id).first()


def get_item_by_id(db: Session, item_id):
    return db.query(TodoItem).filter_by(id=item_id).first()


def create_list(db: Session, data, owner_id):
    todo_list = TodoList(title=data.title, done=data.done, owner_id=owner_id)
    db.add(todo_list)
    db.commit()
    db.refresh(todo_list)
    return todo_list


def create_item(db: Session, data):
    todo_item = TodoItem(body=data.body, done=data.done, list_id=data.list_id)
    db.add(todo_item)
    db.commit()
    db.refresh(todo_item)
    return todo_item


def update_list(db: Session, list_id, data):
    todo_list: TodoList = db.query(TodoList).filter_by(id=list_id).first()

    todo_list.title = data.title
    todo_list.done = data.done

    db.commit()
    db.refresh(todo_list)
    return todo_list


def update_item(db: Session, item_id, data):
    todo_item: TodoItem = db.query(TodoItem).filter_by(id=item_id).first()

    todo_item.body = data.body
    todo_item.done = data.done

    db.commit()
    db.refresh(todo_item)
    return todo_item


def delete_list(db: Session, id):
    db.query(TodoList).filter_by(id=id).delete()
    db.commit()


def delete_item(db: Session, id):
    db.query(TodoItem).filter_by(id=id).delete()
    db.commit()
