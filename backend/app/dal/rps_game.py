from app.models.games import Game, GameTurn, GameTurnAggr
from app.core.schemas import (
    GameSettings,
    GameTurnDetails,
    PlayerAction,
    PlayerSelections,
)
from sqlalchemy.orm import Session

"""
Need to support
- create new game
- get game with uuid (and it's most recent state + aggr)
- evaluate turn
- save game in current state
"""


def create_new_game(game_settings: GameSettings, db: Session):
    new_game = Game(game_settings=game_settings.model_dump(mode="json"))
    db.add(new_game)
    db.commit()
    return new_game


def get_game_token(uuid: str, db: Session):
    game = db.query(Game).filter_by(game_token=uuid).first()
    return game


def get_game_id(id: str, db: Session):
    game = db.query(Game).filter_by(id=id).first()
    return game


def get_game_details(uuid, db: Session):
    game = get_game_token(uuid, db)
    current_turn = (
        db.query(GameTurn).filter_by(game_id=game.id).order_by("updated").first()
    )
    current_points = db.query(GameTurnAggr).filter_by(game_id=game.id).all()

    return {
        "game": {
            "game_id": game.id,
            "game_token": game.game_token,
            "game_settings": game.game_settings,
        },
        "current_turn": (
            {
                "winner": current_turn.winner,
                "in_progress": current_turn.in_progress,
                "turn_details": current_turn.turn_details,
            }
            if current_turn
            else {}
        ),
        "current_points": [
            {"player": point.player, "wins": point.wins} for point in current_points
        ],
    }


def evaluate_and_save_turn(game_state: GameTurnDetails, db: Session):
    winner = evaluate_turn(game_state)
    winner_name = winner.name if winner else None
    gameturn = save_turn(game_state, db, winner_name)

    game_aggr = (
        db.query(GameTurnAggr)
        .filter_by(game_id=game_state.game_id, player=gameturn.winner)
        .first()
    )
    if game_aggr:
        game_aggr.wins += 1
    else:
        game_aggr = GameTurnAggr(
            game_id=game_state.game_id, player=gameturn.winner, wins=1
        )
    db.add(game_aggr)
    db.commit()
    return game_aggr


def evaluate_turn(game_state: GameTurnDetails):
    winner = None
    for player in game_state.actions:
        if not winner:
            winner = player
        else:
            winner = find_winner_rps(winner, player)
    return winner


def check_win_state(game_aggr: GameTurnAggr, game_settings: GameSettings):
    if game_aggr.wins >= game_settings["win_count"] and game_aggr.player:
        return True
    else:
        return False


def save_turn(game_state: GameTurnDetails, db: Session, winner: str, in_progress=False):
    game_turn_json = game_state.model_dump(mode="json")
    gameturn = GameTurn(
        game_id=game_state.game_id,
        turn_details=game_turn_json,
        winner=winner,
        in_progress=in_progress,
    )
    db.add(gameturn)
    db.commit()
    return gameturn


def find_winner_rps(winner: PlayerAction, player: PlayerAction):
    if winner.selection != player.selection:
        if winner.selection == "r":
            new_winner = (
                player if player.selection == PlayerSelections.paper else winner
            )
        elif winner.value == "p":
            new_winner = (
                player if player.selection == PlayerSelections.scissors else winner
            )
        else:
            new_winner = player if player.selection == PlayerSelections.rock else winner
    else:
        new_winner = None
    return new_winner
