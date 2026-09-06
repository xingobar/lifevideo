from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_session
from app.exceptions.not_found_exception import NotFoundException
from app.exceptions.password_error_exception import PasswordErrorException
from app.schemas.auth.create_user import CreateUserRequest
from app.schemas.auth.login_user import LoginUserRequest
from app.schemas.user.create_user_dto import CreateUserDTO
from app.services.user_service import UserService, get_user_service
from app.utils.hash import verify_password
from app.utils.token import create_access_token


class AuthService:
    def __init__(self, session: AsyncSession, user_service: UserService):
        self.session = session
        self.user_service = user_service

    async def register(self, data: CreateUserRequest) -> None:
        await self.user_service.create(
            CreateUserDTO(**data.model_dump(exclude={"password_confirmation"}))
        )
        await self.session.commit()

    async def login(self, data: LoginUserRequest) -> str:
        """會員登入

        Args:
         data (LoginUserRequest) - 登入資料

        Returns:
            str - jwt token

        """
        user = await self.user_service.find_by_account(data.account)

        if user is None:
            raise NotFoundException(message="帳號或密碼錯誤")

        is_match = verify_password(data.password, user.password)

        if is_match is False:
            raise PasswordErrorException()

        return create_access_token({"id": user.id, "account": user.account})


def get_auth_service(session: AsyncSession = Depends(get_session)) -> AuthService:
    return AuthService(session=session, user_service=get_user_service(session))
