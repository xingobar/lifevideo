from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository[T](ABC):
    def __init__(self, session: AsyncSession):
        if not hasattr(self, "model") or self.model is None:
            raise NotImplementedError(f"{self.__class__.__name__} 必須定義 model")
        self.session = session

    @property
    @abstractmethod
    def model(self) -> T:
        pass

    async def find_by_id(self, id: int) -> T:
        """根據 id 抓取資料

        Args:
            id (int): 資料 id

        Returns:
            T: 查詢結果
        """
        return await self.session.get(self.model, id)

    async def delete_by_id(self, data: T) -> None:
        """根據 id 刪除資料

        Args:
            data (T): 要刪除的資料物件
        """
        await self.session.delete(data)
