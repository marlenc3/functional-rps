from app.api.v1.endpoints import endpoint
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(endpoint.router)