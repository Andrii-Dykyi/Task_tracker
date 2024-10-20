import uuid
from typing import Optional

from pydantic_core.core_schema import FieldValidationInfo
from pydantic import BaseModel, EmailStr, field_validator


class UserRegisterRequest(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: EmailStr
    password: str
    password2: str

    @field_validator("password2")
    def passwords_match(cls, v, info: FieldValidationInfo):
        if "password" in info.data and v != info.data["password"]:
            raise ValueError("passwords do not match")
        return v


class UserDetailResponse(BaseModel):
    id: uuid.UUID
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: str
