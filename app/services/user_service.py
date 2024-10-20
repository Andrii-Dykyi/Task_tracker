from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.core.hash import get_password_hash
from app.models.users import User
from app.schemas.users import UserRegisterRequest


async def get_user_by_email(
    session: AsyncSession,
    email: str,
) -> User:
    user = await session.exec(select(User).where(User.email == email))
    return user.first()


async def create_user(
    session: AsyncSession,
    payload: UserRegisterRequest,
) -> User:
    user = User(
        email=payload.email,
        password=get_password_hash(payload.password),
        first_name=payload.first_name,
        last_name=payload.last_name,
    )
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user
