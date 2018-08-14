from rest_framework.exceptions import APIException


class APIGenericException(APIException):
    def __init__(self, msg, code):
        super(APIGenericException, self).__init__(msg)
        self.status_code = code
