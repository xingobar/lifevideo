from app.enums.status_code import StatusCode


class PasswordErrorException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.detail = {
            "code": kwargs.get("code", StatusCode.PASSWORD_ERROR.code),
            "message": kwargs.get("message", StatusCode.PASSWORD_ERROR.message),
        }
