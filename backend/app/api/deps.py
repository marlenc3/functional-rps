from collections.abc import Generator

from fastapi import Security, status
from app.core.config import settings
from app.core.db import session_factory

from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.exceptions import HTTPException

security = HTTPBearer()


def get_db() -> Generator:
    session = session_factory()
    try:
        db = session()
        yield db
    finally:
        db.close()


def validate_api_key(authorization: HTTPAuthorizationCredentials = Security(security)) -> bool:
    api_key = settings.GAME_API_KEY
    if authorization.credentials == api_key:
        return True
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Api Key")
