from typing import Union

from pydantic import BaseModel


class UserFormDataSchema(BaseModel):
    username: str
    password: str


class UserSchemaBase(BaseModel):
    id: int
    username: str


class UserSchemaOrmShow(UserSchemaBase):
    class Config:
        orm_mode = True


class UserSchemaOrm(UserSchemaOrmShow):
    password_hash: str


class TokenSchema(BaseModel):
    access_token: str
    token_type: str


class TokenDataSchema(BaseModel):
    username: Union[str, None] = None
