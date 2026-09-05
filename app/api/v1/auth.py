from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException

from app.enums.status_code import StatusCode
from app.exceptions.user_exist_exception import UserExistException
from app.schemas.auth.create_user_request import CreateUserRequest
from app.schemas.http.response import ApiResponse
from app.services.auth_service import AuthService, get_auth_service

router = APIRouter(prefix="", tags=["auth"])


@router.post(
    "/register", response_model=ApiResponse, status_code=status.HTTP_201_CREATED
)
async def register(
    data: CreateUserRequest, auth_service: AuthService = Depends(get_auth_service)
):
    try:
        await auth_service.register(data)
        return ApiResponse(
            status=StatusCode.SUCCESS.code,
        )
    except UserExistException as ex:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=ex.detail
        ) from ex
