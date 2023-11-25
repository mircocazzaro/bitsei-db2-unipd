class SPARQLExceptions(Exception):
    http_code: int
    code: str
    message: str

    def __init__(
            self,
            http_code: int = 500,
            code: str | None = None,
            message: str = "This is an error message",
    ):
        self.http_code = http_code
        self.code = code or str(self.http_code)
        self.message = message
