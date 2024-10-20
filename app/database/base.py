from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel

from app.core.config import settings
from app.models.boards import Board, UserBoardLink  # noqa: F401
from app.models.tickets import Ticket, UserTicketLink  # noqa: F401
from app.models.users import User  # noqa: F401


def get_database_url():
    user = settings.POSTGRES_USER
    passwd = settings.POSTGRES_PASSWORD
    db_name = settings.POSTGRES_DB
    host = settings.POSTGRES_HOST
    port = settings.POSTGRES_PORT
    return f"postgresql+asyncpg://{user}:{passwd}@{host}:{port}/{db_name}"


engine = create_async_engine(get_database_url())


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
