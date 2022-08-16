import strawberry


@strawberry.type
class User:
    id: int
    username: str


@strawberry.type
class LoginSuccess:
    access_token: str
    token_type: str


@strawberry.type
class LoginError:
    message: str


LoginResult = strawberry.union("LoginResult", (LoginSuccess, LoginError))
