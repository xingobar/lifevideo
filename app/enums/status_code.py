from enum import Enum


class StatusCode(Enum):
    SUCCESS = ("0000", "成功")
    EXISTS = ("4001", "資料已存在")

    def __init__(self, code: str, message: str):
        super().__init__()
        self.code = code
        self.message = message
