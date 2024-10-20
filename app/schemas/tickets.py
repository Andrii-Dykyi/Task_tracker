import uuid

from pydantic import BaseModel


class TicketCreateRequest(BaseModel):
    name: str
    description: str
    board_id: uuid.UUID


class TicketCreateResponse(TicketCreateRequest):
    id: uuid.UUID
    reporter_id: uuid.UUID
