from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_session
from app.schemas.auth.create_user_request import CreateUserRequest
from app.schemas.user.create_user_dto import CreateUserDTO
from app.services.user_service import UserService, get_user_service


class AuthService:
    def __init__(self, session: AsyncSession, user_service: UserService):
        self.session = session
        self.user_service = user_service

    async def register(self, data: CreateUserRequest) -> None:
        await self.user_service.create(
            CreateUserDTO(**data.model_dump(exclude={"password_confirmation"}))
        )
        await self.session.commit()


def get_auth_service(session: AsyncSession = Depends(get_session)) -> AuthService:
    return AuthService(session=session, user_service=get_user_service(session))
