class OpenMovieDatabaseError(Exception):
    def __init__(self, status_code, message,  **kwargs):
        self.status_code = status_code
        super(OpenMovieDatabaseError, self).__init__(message, **kwargs)
