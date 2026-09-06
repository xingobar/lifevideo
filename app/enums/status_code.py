from enum import Enum


class StatusCode(Enum):
    SUCCESS = ("0000", "成功")
    UNAUTHORIZED = ("4001", "尚未登入/登入逾期")
    EXISTS = ("4002", "資料已存在")
    NOT_FOUND = ("4004", "資料不存在")
    PASSWORD_ERROR = ("4005", "密碼錯誤")
    INTERNAL_ERROR = ("5000", "系統錯誤")

    def __init__(self, code: str, message: str):
        super().__init__()
        self.code = code
        self.message = message
