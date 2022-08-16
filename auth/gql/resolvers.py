from datetime import timedelta

from auth.config import ACCESS_TOKEN_EXPIRE_MINUTES
from auth.dependencies import authenticate_user, create_access_token
from auth.gql.types import LoginResult, LoginError, LoginSuccess


def login_resolver(root, info, username: str, password: str) -> LoginResult:
    db = info.context['db']
    user = authenticate_user(db, username, password)

    if user is None:
        return LoginError(message="Something went wrong")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return LoginSuccess(access_token=access_token, token_type='bearer')


# mutation {
#   login(username: "aliaksei", password: "123456") {
#     ... on LoginSuccess {
#       user {
#         id,
#         username
#       }
#     }
#     ... on LoginError {
#       message
#     }
#   }
# }