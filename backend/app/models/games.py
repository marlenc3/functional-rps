import enum
import uuid

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


class Game(Base):
    __tablename__ = 'game'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    game_settings = Column(JSON, default=dict)
    game_token = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True)
    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

class GameTurn(Base):
    __tablename__ = 'gameturn'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    game_id = Column(Integer, nullable=False, index=True)
    # player : x, player: y
    winner = Column(String, nullable=True)
    turn_details = Column(JSON, default=dict)
    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

class GameTurnAggr(Base):
    __tablename__ = 'gameturn_aggregation'

    game_id = Column(Integer, nullable=False, index=True)
    player = Column(String, nullable=False)
    wins = Column(Integer, nullable=False, default=0)
    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
