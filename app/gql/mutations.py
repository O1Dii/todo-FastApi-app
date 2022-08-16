from typing import Optional

import strawberry

import app.gql.types as todos_types
from app.crud import create_list, update_list
from app.schemas import TodoListSchemaBase


@strawberry.input
class TodoInput:
    title: str
    done: bool
    id: Optional[strawberry.ID] = None


def resolve_todo_list_mutation(root, info, data: TodoInput) -> todos_types.TodoList:
    db = info.context['db']
    user = info.context['current_user']
    # one way
    # data = TodoListSchemaBase(title=data.title, done=data.done)
    if data.id is not None:
        list_item = update_list(db, data.id, data)
    else:
        list_item = create_list(db, data, user.id)
    return list_item
