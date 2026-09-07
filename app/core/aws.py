from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

import aioboto3

from app.core.config import settings

_session = aioboto3.Session(
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    region_name=settings.AWS_DEFAULT_REGION,
)


@asynccontextmanager
async def get_s3_client() -> AsyncGenerator:
    async with _session.client("s3", endpoint_url=settings.AWS_ENDPOINT_URL) as client:
        yield client


@asynccontextmanager
async def get_sqs_client() -> AsyncGenerator:
    async with _session.client("sqs", endpoint_url=settings.AWS_ENDPOINT_URL) as client:
        yield client
