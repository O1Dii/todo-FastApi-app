from typing import List

import strawberry

from app.crud import get_list_by_id


@strawberry.type
class TodoItem:
    id: int
    body: str
    done: bool


def resolve_todo_items(root, info) -> List[TodoItem]:
    db = info.context['db']
    list_item = get_list_by_id(db, root.id)
    return list_item.items


@strawberry.type
class TodoList:
    id: int
    title: str
    done: bool
    owner_id: int
    items: List[TodoItem] = strawberry.field(resolver=resolve_todo_items)
