from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database.session import get_session
from app.schemas.users import UserRegisterRequest, UserDetailResponse
from app.services.user_service import get_user_by_email, create_user


router = APIRouter(prefix="/users")


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(
    payload: UserRegisterRequest,
    session: AsyncSession = Depends(get_session),
) -> UserDetailResponse:
    existing_user = await get_user_by_email(session, payload.email)

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists",
        )

    user = await create_user(session, payload)
    return user
