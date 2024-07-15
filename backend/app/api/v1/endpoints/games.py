from fastapi import APIRouter

from app.models import Game
from app.core.schemas import GameSettings, GameTurn
from app.api.deps import validate_api_key

router = APIRouter()

"""
main apis that we'll likely need
- create game
- save game 
- save turn
- check turn 
- get game
- update game

    main workflow ->
     - if no uuid, ask to make new game. 
     - fill out config, which should just be user1, and or user2 (select if comptuer is playing)
     - start game (save config)
     - first turn - nturn where 1 player has > n wins
     - at anytime can save, and will be given a uuid to return to game
"""
# dependencies=[Depends(validate_api_key)]


@router.get("/game/{game_uuid}")
def get_game(game_uuid):
    """
    given a uuid, return back the Game Settings, Current Results, and Current Turn
    :param game_uuid:
    :return: game settings, results and turn
    """
    pass


@router.post("/start-game")
def start_game(game: GameSettings):
    """

    :param game: given settings, set up game
    :return: uuid
    """
    pass


@router.post("/evaluate-turn")
def evaluate_turn(game: GameTurn):
    """
    take in list of actions, save and return the result, and let user know if they won
    :param game:
    :return:
    """
    pass


@router.post("/save-game")
def save_game(game: GameTurn):
    """
    could take in empty turn, and would just return 200, else save current turn
    :param game:
    :return:
    """
    pass
