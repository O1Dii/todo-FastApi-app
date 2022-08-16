import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from app.routes import router as app_router
from auth.routes import router as auth_router
from gql import Query, Mutation, get_context

schema = strawberry.Schema(Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema, context_getter=get_context)

# basically unusable
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(app_router)
app.include_router(auth_router)
app.include_router(graphql_app, prefix="/graphql")
