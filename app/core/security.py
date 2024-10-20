from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database.session import get_session
from app.models.users import User
from app.services.user_service import get_user_by_email

from .hash import verify_password



async def authenticate_user(
    session: AsyncSession, email: str, password: str
) -> User:
    user = await get_user_by_email(session, email)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


async def get_current_user(
    credentials: Annotated[HTTPBasicCredentials, Depends(HTTPBasic())],
    session: AsyncSession = Depends(get_session),
):
    user = await authenticate_user(session, credentials.username, credentials.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized"
        )
    return user


def allow_roles_access(*roles):
    async def check_role(user: User = Depends(get_current_user)):
        if roles and user.role.value not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You don't have enough permissions",
            )
        return user

    return check_role
