import typing

import strawberry
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.requests import Request
from starlette.websockets import WebSocket
from strawberry import BasePermission
from strawberry.types import Info

from app.gql.mutations import resolve_todo_list_mutation
from app.gql.resolvers import resolve_todo_list
from app.gql.types import TodoList
from auth.config import oauth2_scheme
from auth.dependencies import get_current_user
from auth.gql.resolvers import login_resolver
from auth.gql.types import LoginResult
from dependencies import get_db


# context can be a class
# if you don't want db to be in all requests, for example
async def get_context(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):
    return {
        "db": db,
        "auth_token": token
    }


class IsAuthenticated(BasePermission):
    message = "User is not authenticated"

    async def has_permission(self, source: typing.Any, info: Info, **kwargs) -> bool:
        # context also contains request, response and background_tasks
        request: typing.Union[Request, WebSocket] = info.context["request"]
        token: str = info.context['auth_token']
        db = info.context['db']

        current_user = None
        try:
            current_user = await get_current_user(token, db)
        except HTTPException:
            pass
        if not current_user:
            return False

        info.context['current_user'] = current_user
        return True


@strawberry.type
class Query:
    todo_list: TodoList = strawberry.field(resolver=resolve_todo_list, permission_classes=[IsAuthenticated])


@strawberry.type
class Mutation:
    # better to name them with action, same for query
    todo_list: TodoList = strawberry.mutation(resolver=resolve_todo_list_mutation, permission_classes=[IsAuthenticated])
    login: LoginResult = strawberry.mutation(resolver=login_resolver)
