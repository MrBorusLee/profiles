from typing import Annotated

import asyncpg
from asyncpg import Connection
from fastapi import Depends

from profiles.settings import settings


async def get_db():
    conn = await asyncpg.connect(
        database=settings.database.postgres_db,
        host=settings.database.postgres_host,
        port=settings.database.postgres_port,
        password=settings.database.postgres_password,
        user=settings.database.postgres_user,
    )
    yield conn
    await conn.close()


DBSession = Annotated[Connection, Depends(get_db)]
