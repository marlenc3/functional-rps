import os

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

Base = declarative_base()


def session_factory():
    engine = create_engine(settings.POSTGRES_DB)
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)
