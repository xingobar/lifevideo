from pydantic import BaseModel


class ApiResponse[T](BaseModel):
    status: str
    data: T = {}
