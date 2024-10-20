from enum import Enum
from typing import Optional

from pydantic import EmailStr
from sqlmodel import Field, Relationship

from .base import BaseModel
from .boards import Board, UserBoardLink
from .tickets import Ticket, UserTicketLink


class UserRoles(str, Enum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"


class User(BaseModel, table=True):
    __tablename__ = "users"

    email: EmailStr = Field(unique=True)
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    password: str
    role: UserRoles = UserRoles.USER.value
    boards: list["Board"] = Relationship(
        back_populates="users",
        link_model=UserBoardLink,
    )
    reported_tickets: list["Ticket"] = Relationship(back_populates="reporter")
    assigned_tickets: list["Ticket"] = Relationship(
        back_populates="assignees",
        link_model=UserTicketLink,
    )
