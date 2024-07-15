from fastapi import FastAPI
from app.core.config import settings
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

from app.api.v1.router import api_router
from app.api.v1.metadata import tags


def create_app():
    app = FastAPI(
        title="Fucntional Rock Paper Scissors",
        version="0.0.1",
        openapi_url="/api/openapi.json",
        docs_url="/api/docs",
        openapi_tags=tags.tags_metadata,
    )

    app.include_router(api_router, prefix=settings.API_V1_STR)
    return app


app = create_app()
