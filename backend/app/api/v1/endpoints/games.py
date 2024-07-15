import json
from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.core.schemas import (
    GameSettings,
    GameTurnDetails,
    TurnResultResponse,
    GameResponse,
)
from app.dal.rps_game import (
    get_game_details,
    create_new_game,
    evaluate_and_save_turn,
    check_win_state,
    get_game_id,
)

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


@router.get("/game/{game_uuid}")
def get_game(game_uuid, db: Session = Depends(get_db)):
    """
    given a uuid, return back the Game Settings, Current Results, and Current Turn
    :param db:
    :param game_uuid:
    :return: game settings, results and turn
    """
    game_details = get_game_details(uuid=game_uuid, db=db)
    return game_details


@router.post("/start-game")
def start_game(game: GameSettings, db: Session = Depends(get_db)):
    """

    :param db:
    :param game: given settings, set up game
    :return: uuid
    """
    game = create_new_game(game, db=db)
    return Response(
        status_code=status.HTTP_201_CREATED,
        content={"game_token": game.game_token, "game_id": game.game_id},
    )


@router.post("/evaluate-turn")
def evaluate_turn(game: GameTurnDetails, db: Session = Depends(get_db)):
    """
    take in list of actions, save and return the result, and let user know if they won
    :param db:
    :param game:
    :return:
    """
    current_score = evaluate_and_save_turn(game, db)
    game_settings = get_game_id(current_score.game_id, db).game_settings
    game_won = check_win_state(current_score, game_settings)
    response_result = TurnResultResponse(
        won=game_won,
        game_id=current_score.game_id,
        current_score={current_score.player: current_score.wins},
    ).json()
    return Response(status_code=status.HTTP_200_OK, content=response_result)


@router.post("/save-game")
def save_game(game: GameTurnDetails, db: Session = Depends(get_db)):
    """
    could take in empty turn, and would just return 200, else save current turn
    :param db:
    :param game:
    :return:
    """
    pass
