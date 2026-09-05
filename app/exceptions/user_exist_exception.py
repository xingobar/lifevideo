from app.enums.status_code import StatusCode


class UserExistException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.detail = {
            "code": kwargs.get("code", StatusCode.EXISTS.code),
            "message": kwargs.get("message", StatusCode.EXISTS.message),
        }
