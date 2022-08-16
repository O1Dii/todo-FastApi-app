from typing import List

from pydantic import BaseModel


class TodoItemSchemaBase(BaseModel):
    body: str
    done: bool


class TodoItemWithListIdSchema(TodoItemSchemaBase):
    list_id: int


class TodoListSchemaBase(BaseModel):
    title: str
    done: bool


class TodoItemSchemaOrm(TodoItemSchemaBase):
    id: int

    class Config:
        orm_mode = True


class TodoListSchemaOrm(TodoListSchemaBase):
    id: int
    owner_id: int
    items: List[TodoItemSchemaOrm] = []

    class Config:
        orm_mode = True


class DeleteBodySchema(BaseModel):
    id: int
