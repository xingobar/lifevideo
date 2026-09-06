from datetime import datetime, timedelta, timezone

import jwt

from app.core.config import settings


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """建立 access token

    Args:
        data (dict): token data
        expires_delta (timedelta | None): 過期時間

    Returns:
        str: access token

    """
    if expires_delta is None:
        expires_delta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {**data, "exp": datetime.now(timezone.utc) + expires_delta}

    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
