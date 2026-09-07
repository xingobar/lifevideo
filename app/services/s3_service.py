from fastapi import UploadFile

from app.core.aws import get_s3_client
from app.core.config import settings


class S3Service:
    _bucket = settings.AWS_BUCKET

    @property
    def bucket(self) -> str:
        return self._bucket

    @bucket.setter
    def bucket(self, val):
        self._bucket = val

    async def get_object(self, key: str) -> bytes:
        """取得物件

        Args:
            key (str): 物件路徑

        Returns:
            bytes: 物件內容

        """
        async with get_s3_client() as s3:
            response = await s3.get_object(Bucket=self.bucket, Key=key)

            async with response["Body"] as stream:
                return await stream.read()

    async def upload_object(self, key: str, file: UploadFile) -> None:
        """上傳物件

        Args:
            key (str): 物件路徑
            file (UploadFile): 上傳檔案

        Returns:
            None

        """
        content: bytes = await file.read()

        async with get_s3_client() as s3:
            await s3.put_object(
                Bucket=self.bucket,
                Key=key,
                Body=content,
                ContentType=file.content_type or "application/octet-stream",
            )


def get_s3_service() -> S3Service:
    return S3Service()
