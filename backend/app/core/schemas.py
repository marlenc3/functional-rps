import enum

from pydantic import BaseModel
from typing import List, Optional
from enum import Enum


class GameSettings(BaseModel):
    type: str = "rps"
    players: List[str]
    win_count = int


class PlayerSelections(Enum):
    rock = 'r'
    paper = 'p'
    scissors = 's'


class PlayerAction(BaseModel):
    name: str
    value: PlayerSelections


class GameTurn(BaseModel):
    game_uuid: str
    actions = List[PlayerAction]

