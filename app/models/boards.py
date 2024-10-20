import uuid
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship

from .base import BaseModel

if TYPE_CHECKING:
    from .tickets import Ticket
    from .users import User


class UserBoardLink(BaseModel, table=True):
    __tablename__ = "users_boards"

    user_id: uuid.UUID = Field(default=None, foreign_key="users.id", primary_key=True)
    board_id: uuid.UUID = Field(default=None, foreign_key="boards.id", primary_key=True)


class Board(BaseModel, table=True):
    __tablename__ = "boards"

    name: str
    description: str
    users: list["User"] = Relationship(back_populates="boards", link_model=UserBoardLink)
    tickets: list["Ticket"] = Relationship(back_populates="board")
