from http.client import HTTPException

from starlette import status


class NotFoundException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_404_NOT_FOUND
        self.detail = "Not Found"
