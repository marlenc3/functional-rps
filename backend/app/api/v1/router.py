from app.api.v1.endpoints import endpoint
from app.api.v1.endpoints import games
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(endpoint.router)
api_router.include_router(games.router)
