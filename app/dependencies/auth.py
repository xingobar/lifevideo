import jwt
from fastapi import Depends, status
from fastapi.exceptions import HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.db.session import get_session
from app.enums.status_code import StatusCode
from app.models.user import User
from app.services.user_service import get_user_service

security = HTTPBearer()


def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> dict | None:
    """驗證 token"""
    credential = credentials.credentials
    try:
        return jwt.decode(
            credential, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"code": StatusCode.UNAUTHORIZED.code, "message": "Token 已過期"},
        ) from jwt.ExpiredSignatureError
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"code": StatusCode.UNAUTHORIZED.code, "message": "Token 無效"},
        ) from jwt.InvalidTokenError


async def get_current_user(
    session: AsyncSession = Depends(get_session),
    credential: dict | None = Depends(verify_token),
) -> User | None:
    """取得目前的使用者"""
    user_service = get_user_service(session)
    user = await user_service.find_by_id(credential["id"])

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "code": StatusCode.NOT_FOUND.code,
                "message": StatusCode.NOT_FOUND.message,
            },
        )

    return user
