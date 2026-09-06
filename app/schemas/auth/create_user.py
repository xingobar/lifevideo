from typing import Self

from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator


class CreateUserRequest(BaseModel):
    account: str = Field(description="帳號")
    email: EmailStr = Field(description="電子郵件")
    password: str = Field(description="密碼")
    password_confirmation: str = Field(description="確認密碼")

    @field_validator("password")
    @classmethod
    def password_min_length(cls, value: str) -> str:
        if len(value) < 6:
            raise ValueError("密碼至少 6 個字元")
        return value

    @field_validator("password")
    @classmethod
    def password_max_length(cls, value: str) -> str:
        if len(value) > 20:
            raise ValueError("密碼至多 20 個字元")
        return value

    @field_validator("account")
    @classmethod
    def account_max_length(cls, value: str) -> str:
        if len(value) > 50:
            raise ValueError("密碼至多 50 個字元")
        return value

    @model_validator(mode="after")
    def check_password_match(self) -> Self:
        if self.password != self.password_confirmation:
            raise ValueError("密碼不一致")
        return self
