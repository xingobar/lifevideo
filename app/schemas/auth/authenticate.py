from pydantic import BaseModel, ConfigDict, Field


class AuthenticateResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(description="用戶 id", examples=[1])
    account: str = Field(description="用戶帳號", examples=["user@example.com"])
