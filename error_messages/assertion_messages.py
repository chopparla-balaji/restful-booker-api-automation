from typing import Final


class AssertionMessages:

    AUTH_FAILED:Final[str] = "Authentication failed"
    RESP_BODY:Final[str] = "Response body should not be empty"
    TOKEN_KEY_MISSING:Final[str] = "Token key missing"
    TOKEN_EMPTY:Final[str] = "Token should not be empty"