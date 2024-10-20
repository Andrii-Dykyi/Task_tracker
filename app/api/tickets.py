from fastapi import APIRouter, Depends, status, BackgroundTasks, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession

from app.core.security import allow_roles_access
from app.database.session import get_session
from app.models.users import User
from app.schemas.tickets import TicketCreateRequest, TicketCreateResponse
from app.services.ticket_service import create_ticket
from app.services.board_service import get_board_by_id
from app.tasks.emails import send_notification_email


router = APIRouter(prefix="/tickets")


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_ticket_view(
    payload: TicketCreateRequest,
    background_tasks: BackgroundTasks,
    session: AsyncSession = Depends(get_session),
    current_user: User = Depends(allow_roles_access("user")),
) -> TicketCreateResponse:
    board = await get_board_by_id(session, payload.board_id)
    if not board:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Board does not exist.")

    ticket = await create_ticket(session, payload, current_user)

    # sending a notification email
    background_tasks.add_task(
        send_notification_email,
        current_user.email,
        f"Ticket {ticket.name} has been created",
        f"Ticket description: {ticket.description}",
    )
    return ticket
