from app.enums.status_code import StatusCode


class UnAuthorizationException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.detail = {
            "code": kwargs.get("code", StatusCode.UNAUTHORIZED.code),
            "message": kwargs.get("message", StatusCode.UNAUTHORIZED.message),
        }
