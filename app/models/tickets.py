import uuid
from enum import Enum
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship

from .base import BaseModel

if TYPE_CHECKING:
    from .boards import Board
    from .users import User


class UserTicketLink(BaseModel, table=True):
    __tablename__ = "users_tickets"

    user_id: uuid.UUID = Field(default=None, foreign_key="users.id", primary_key=True)
    ticket_id: uuid.UUID = Field(
        default=None,
        foreign_key="tickets.id",
        primary_key=True,
    )


class TicketStatus(str, Enum):
    TODO = "TODO"
    IN_PROGRESS = "In Progress"
    DONE = "Done"


class TicketPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class Ticket(BaseModel, table=True):
    __tablename__ = "tickets"

    name: str
    description: str
    status: TicketStatus = Field(default="TODO")
    priority: TicketPriority = Field(default="medium")
    board_id: uuid.UUID = Field(foreign_key="boards.id")
    board: "Board" = Relationship(back_populates="tickets")
    reporter_id: uuid.UUID = Field(foreign_key="users.id")
    reporter: "User" = Relationship(back_populates="reported_tickets")
    assignees: list["User"] = Relationship(
        back_populates="assigned_tickets",
        link_model=UserTicketLink,
    )
