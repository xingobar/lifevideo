from sqlalchemy.ext.asyncio import AsyncSession

from app.exceptions.user_exist_exception import UserExistException
from app.repositories.user_repository import UserRepository, get_user_repository
from app.schemas.user.create_user_dto import CreateUserDTO
from app.utils.hash import hash_password


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def create(self, data: CreateUserDTO) -> None:
        exists = await self.user_repository.check_account_or_email_exists(
            data.account, data.email
        )

        if exists:
            raise UserExistException(message="會員資料已存在")

        await self.user_repository.create(
            CreateUserDTO(**{**vars(data), "password": hash_password(data.password)})
        )


def get_user_service(session: AsyncSession) -> UserService:
    return UserService(user_repository=get_user_repository(session))
