from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException

from app.enums.status_code import StatusCode
from app.exceptions.not_found_exception import NotFoundException
from app.exceptions.password_error_exception import PasswordErrorException
from app.exceptions.user_exist_exception import UserExistException
from app.schemas.auth.create_user_request import CreateUserRequest
from app.schemas.auth.login_user_request import LoginUserRequest, LoginUserResponse
from app.schemas.http.response import ApiResponse
from app.services.auth_service import AuthService, get_auth_service

router = APIRouter(prefix="", tags=["auth"])


@router.post(
    "/register",
    response_model=ApiResponse,
    status_code=status.HTTP_201_CREATED,
    summary="會員註冊",
    description="會員註冊",
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


@router.post(
    "/login",
    status_code=status.HTTP_200_OK,
    summary="會員登入",
    description="會員登入",
    response_model=LoginUserResponse,
)
async def login(
    data: LoginUserRequest, auth_service: AuthService = Depends(get_auth_service)
):
    try:
        token = await auth_service.login(data)

        return {"access_token": token}
    except PasswordErrorException as ex:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=ex.detail
        ) from ex
    except NotFoundException as ex:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=ex.detail
        ) from ex
