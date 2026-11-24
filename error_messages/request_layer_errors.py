from typing import Final

class RequestLayerErrors:

    URL_EMPTY:Final[str]  = "url cannot be None"
    PARAM_TYPE:Final[str] = "params must be contains key and value"
    PARAM_LENGTH:Final[str] = "params length must be greater than 0"
    HEADERS_TYPE:Final[str] = "headers must be contains key and value"
    HEADERS_LENGTH:Final[str] = "headers length must be greater than 0"
    DATA_ERR:Final[str] = "data must be contains key and value"