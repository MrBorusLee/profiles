import logging
from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from profiles.api.deps import get_db

# Metrics, healthcheck, etc.
meta_router = APIRouter(tags=["meta"])

HEALTHCHECK_ENDPOINT = "/healthcheck/"


class EndpointFilter(logging.Filter):
    def __init__(
        self,
        path: str,
        *args: Any,
        **kwargs: Any,
    ):
        super().__init__(*args, **kwargs)
        self._path = path

    def filter(self, record: logging.LogRecord) -> bool:
        return record.getMessage().find(self._path) == -1


# Add filter to the logger
uvicorn_logger = logging.getLogger("uvicorn.access")
uvicorn_logger.addFilter(EndpointFilter(path=HEALTHCHECK_ENDPOINT))


@meta_router.get(HEALTHCHECK_ENDPOINT)
async def healthcheck(db: AsyncSession = Depends(get_db)):
    await db.execute(text("select 1"))
    return "ok"
