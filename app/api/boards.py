from fastapi import APIRouter, Depends, status
from sqlmodel.ext.asyncio.session import AsyncSession

from app.core.security import allow_roles_access
from app.database.session import get_session
from app.models.users import User
from app.schemas.boards import BoardCreateRequest, BoardCreateResponse
from app.services.board_service import create_board


router = APIRouter(prefix="/boards")


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_board_view(
    payload: BoardCreateRequest,
    session: AsyncSession = Depends(get_session),
    current_user: User = Depends(allow_roles_access("user")),
) -> BoardCreateResponse:
    board = await create_board(session, payload, current_user)
    return board
