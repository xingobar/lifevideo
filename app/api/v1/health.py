from fastapi import APIRouter, Depends
from redis.asyncio import Redis
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.redis import get_redis
from app.db.session import get_session

router = APIRouter(prefix="/health", tags=["health"])


@router.get("")
async def health_check(
    session: AsyncSession = Depends(get_session),
    redis: Redis = Depends(get_redis),
):
    await session.execute(text("SELECT 1"))
    await redis.ping()
    return {"status": "ok", "postgres": "ok", "redis": "ok"}
