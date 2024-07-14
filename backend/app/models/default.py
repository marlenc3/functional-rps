from app.core.db import Base

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Boolean
)

from sqlalchemy.dialects.postgresql import JSON, UUID
from sqlalchemy.schema import Index
from sqlalchemy.sql import expression, func

class View(Base):
    __tablename__ = 'view'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    payload = Column(JSON, default=dict)
    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
