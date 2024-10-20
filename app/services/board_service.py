import uuid

from sqlmodel.ext.asyncio.session import AsyncSession

from app.models.boards import Board
from app.models.users import User
from app.schemas.boards import BoardCreateRequest


async def get_board_by_id(
    session: AsyncSession,
    board_id: uuid.UUID,
) -> Board | None:
    board = await session.get(Board, board_id)
    return board


async def create_board(
    session: AsyncSession,
    payload: BoardCreateRequest,
    user: User,
) -> Board:
    board = Board(name=payload.name, description=payload.description, users=[user])
    session.add(board)
    await session.commit()
    await session.refresh(board)
    return board
