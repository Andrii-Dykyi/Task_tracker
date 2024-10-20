from sqlmodel.ext.asyncio.session import AsyncSession

from app.models.tickets import Ticket
from app.models.users import User
from app.schemas.tickets import TicketCreateRequest


async def create_ticket(
    session: AsyncSession,
    payload: TicketCreateRequest,
    user: User,
) -> Ticket:
    ticket = Ticket(
        name=payload.name,
        description=payload.description,
        board_id=payload.board_id,
        reporter=user
    )
    session.add(ticket)
    await session.commit()
    await session.refresh(ticket)
    return ticket
