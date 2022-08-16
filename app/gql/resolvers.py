from typing import Optional, List

import strawberry

from app.crud import get_list_by_id, get_lists_for_user
import app.gql.types as todos_types


def resolve_todo_list(root, info, id: Optional[strawberry.ID] = None) -> List[todos_types.TodoList]:
    if id is not None:
        db = info.context['db']
        list_item = get_list_by_id(db, id)
        return [todos_types.TodoList(id=list_item.id, title=list_item.title, done=list_item.done, owner_id=list_item.owner_id)]
    else:
        db = info.context['db']
        user = info.context['current_user']
        lists = get_lists_for_user(db, user.id)
        return [todos_types.TodoList(id=item.id, title=item.title, done=item.done, owner_id=item.owner_id) for item in lists]
