from app.enums.status_code import StatusCode


class NotFoundException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.detail = {
            "code": kwargs.get("code", StatusCode.NOT_FOUND.code),
            "message": kwargs.get("message", StatusCode.NOT_FOUND.message),
        }
