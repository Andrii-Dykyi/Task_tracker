import uuid

from pydantic import BaseModel


class BoardCreateRequest(BaseModel):
    name: str
    description: str


class BoardCreateResponse(BoardCreateRequest):
    id: uuid.UUID
