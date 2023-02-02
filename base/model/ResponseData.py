from typing import Optional


class ResponseData:
    data: Optional[object]
    message: Optional[str]
    status_code: Optional[int]

    def __init__(self, data, message, status_code):
        self.data = data
        self.message = message
        self.status_code = status_code

