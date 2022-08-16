import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
SQLALCHEMY_DATABASE_URL = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@localhost:65432/db'


# working with alembic:
# alembic revision --autogenerate -m "migration message" - creating a migration
# alembic upgrade heads - upgrade
# alembic downgrade - downgrade
# alembic downgrade base - downgrade all

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

from models import *
