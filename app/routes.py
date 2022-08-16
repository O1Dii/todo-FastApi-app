from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud import get_lists_for_user, create_list, create_item, get_list_by_id, delete_list, delete_item, \
    get_item_by_id, update_list, update_item
from app.schemas import TodoListSchemaBase, TodoListSchemaOrm, TodoItemSchemaBase, DeleteBodySchema, \
    TodoItemWithListIdSchema, TodoItemSchemaOrm
from auth.dependencies import get_current_user
from auth.schemas import UserSchemaOrm
from dependencies import get_db

router = APIRouter(tags=['todo'])


@router.get('/lists', response_model=List[TodoListSchemaOrm])
def get_items_endpoint(current_user: UserSchemaOrm = Depends(get_current_user), db: Session = Depends(get_db)):
    return get_lists_for_user(db, current_user.id)


@router.get('/lists/{item_id}', response_model=TodoListSchemaOrm)
def get_list_endpoint(item_id: int, current_user: UserSchemaOrm = Depends(get_current_user), db: Session = Depends(get_db)):
    return get_list_by_id(db, item_id)


@router.get('/items/{item_id}', response_model=TodoItemSchemaOrm)
def get_item_endpoint(item_id: int, current_user: UserSchemaOrm = Depends(get_current_user), db: Session = Depends(get_db)):
    return get_item_by_id(db, item_id)


@router.post('/lists/create', response_model=TodoListSchemaOrm)
def create_list_endpoint(request: TodoListSchemaBase, current_user: UserSchemaOrm = Depends(get_current_user), db: Session = Depends(get_db)):
    return create_list(db, data=request, owner_id=current_user.id)


@router.post('/items/create', response_model=TodoListSchemaOrm)
def create_item_endpoint(request: TodoItemWithListIdSchema, current_user: UserSchemaOrm = Depends(get_current_user), db: Session = Depends(get_db)):
    create_item(db, request)
    return get_list_by_id(db, request.list_id)


@router.put('/lists/{item_id}', response_model=TodoListSchemaOrm)
def update_list_endpoint(item_id: int, request: TodoListSchemaBase, current_user: UserSchemaOrm = Depends(get_current_user), db: Session = Depends(get_db)):
    return update_list(db, item_id, data=request)


@router.put('/items/{item_id}', response_model=TodoItemSchemaOrm)
def update_item_endpoint(item_id: int, request: TodoItemWithListIdSchema, current_user: UserSchemaOrm = Depends(get_current_user), db: Session = Depends(get_db)):
    return update_item(db, item_id, request)


@router.delete('/lists/{item_id}')
def delete_list_endpoint(item_id: int, current_user: UserSchemaOrm = Depends(get_current_user), db: Session = Depends(get_db)):
    delete_list(db, item_id)
    return {'success': 1}


@router.delete('/items/{item_id}')
def delete_item_endpoint(item_id: int, current_user: UserSchemaOrm = Depends(get_current_user), db: Session = Depends(get_db)):
    delete_item(db, item_id)
    return {'success': 1}
