from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.v1 import health
from app.core.config import settings
from app.db.redis import redis_client


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await redis_client.aclose()


app = FastAPI(
    title="LifeVideo API",
    debug=settings.APP_DEBUG,
    lifespan=lifespan,
)

app.include_router(health.router, prefix="/api/v1")
