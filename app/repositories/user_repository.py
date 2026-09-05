from sqlalchemy import exists, or_, select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.repositories.base_repository import BaseRepository
from app.schemas.user.create_user_dto import CreateUserDTO


class UserRepository(BaseRepository[User]):
    @property
    def model(self) -> type[User]:
        return User

    async def create(self, data: CreateUserDTO) -> None:
        self.session.add(self.model(**vars(data)))

    async def check_account_or_email_exists(self, account: str, email: str) -> bool:
        """檢查帳號/電子郵件是否存在

        Args:
            account (str): 帳號
            email (str): 電子郵件

        Returns:
            bool: 資料存在

        """
        result: Result = await self.session.execute(
            select(
                exists().where(
                    or_(self.model.account == account, self.model.email == email)
                )
            )
        )

        return result.scalar()

    async def find_by_account(self, account: str) -> User | None:
        """根據帳號取得資料

        Args:
            account (str): 帳號

        Returns:
            User | None: 會員資料

        """
        result: Result = await self.session.execute(
            select(self.model).where(self.model.account == account)
        )

        return result.scalar()


def get_user_repository(session: AsyncSession) -> UserRepository:
    return UserRepository(session)
