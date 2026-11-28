from typing import Final


class ResponseLayerErrors:

    STATUS_CODE: str = "Request failed: Expected status code 200, but received {0}"
    CONTENT_TYPE_NOT_MATCH: Final[str] = "Request failed: Expected and received Content-Type do not match."