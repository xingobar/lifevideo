from sqlalchemy.ext.asyncio import AsyncSession

from app.exceptions.user_exist_exception import UserExistException
from app.models.user import User
from app.repositories.user_repository import UserRepository, get_user_repository
from app.schemas.user.create_user_dto import CreateUserDTO
from app.utils.hash import hash_password


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def create(self, data: CreateUserDTO) -> None:
        """新增會員

        Args:
            data (CreateUserDTO): 新增會員 dto

        Returns:
            None

        """
        exists = await self.user_repository.check_account_or_email_exists(
            data.account, data.email
        )

        if exists:
            raise UserExistException(message="會員資料已存在")

        await self.user_repository.create(
            CreateUserDTO(**{**vars(data), "password": hash_password(data.password)})
        )

    async def find_by_account(self, account: str) -> User | None:
        """根據帳號取得資料

        Args:
            account (str): 帳號

        Returns:
            User | None: 會員資料

        """
        return await self.user_repository.find_by_account(account)


def get_user_service(session: AsyncSession) -> UserService:
    return UserService(user_repository=get_user_repository(session))
