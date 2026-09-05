from pydantic import BaseModel, Field


class LoginUserRequest(BaseModel):
    account: str = Field(description="帳號")
    password: str = Field(description="密碼")


class LoginUserResponse(BaseModel):
    token_type: str = Field(description="token 類型", default="Bearer")
    access_token: str = Field(description="access token")
