from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.api.v1 import auth, health
from app.core.config import settings
from app.db.redis import redis_client
from app.enums.status_code import StatusCode


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await redis_client.aclose()


app = FastAPI(
    title="LifeVideo API",
    debug=settings.APP_DEBUG,
    lifespan=lifespan,
)


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "status": StatusCode.INTERNAL_ERROR.code,
            "message": StatusCode.INTERNAL_ERROR.message,
        },
    )


app.include_router(health.router, prefix="/api/v1")
app.include_router(auth.router, prefix="/api/v1/auth")
