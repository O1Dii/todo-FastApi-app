from datetime import timedelta
from typing import List

from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from auth.config import ACCESS_TOKEN_EXPIRE_MINUTES
from auth.crud import create_user, get_all_users, get_user
from auth.dependencies import authenticate_user, create_access_token, get_current_user
from auth.schemas import TokenSchema, UserSchemaBase, UserFormDataSchema, UserSchemaOrm, UserSchemaOrmShow
from dependencies import get_db

router = APIRouter(prefix='/auth', tags=['auth'])


@router.post("/token", response_model=TokenSchema)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/registration", response_model=UserSchemaOrmShow)
def register(request: UserFormDataSchema, db: Session = Depends(get_db)):
    already_exists_exception = HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="Username already exists",
        headers={"WWW-Authenticate": "Bearer"},
    )
    user = get_user(db, request.username)
    if user:
        raise already_exists_exception
    return create_user(db, request)


@router.get("/get_me", response_model=UserSchemaOrmShow)
def read_users_me(current_user: UserSchemaOrm = Depends(get_current_user)):
    return current_user


@router.get("/users", response_model=List[UserSchemaOrmShow])
def read_users_me(current_user: UserSchemaOrm = Depends(get_current_user), db: Session = Depends(get_db)):
    return get_all_users(db)
