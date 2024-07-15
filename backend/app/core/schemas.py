import enum

from pydantic import BaseModel
from typing import List, Optional
from enum import Enum
from datetime import datetime

from app.models.games import GameTurn, GameTurnAggr


class GameSettings(BaseModel):
    type: str = "rps"
    players: List[str]
    win_count: int


class PlayerSelections(str, Enum):
    rock = "r"
    paper = "p"
    scissors = "s"


class PlayerAction(BaseModel):
    name: str
    selection: PlayerSelections


class GameTurnDetails(BaseModel):
    game_id: int
    actions: List[PlayerAction]


class GameResponse(BaseModel):
    game_id: int
    current_turn: dict
    current_scores: List[dict]


class TurnResultResponse(BaseModel):
    game_id: int
    current_score: dict
    won: bool
