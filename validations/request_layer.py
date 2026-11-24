from error_messages.request_layer_errors import RequestLayerErrors
from utils.exceptions import raise_exception


class RequestLayer:

    def validate_request_data(self, end_point:str, params:dict[str, str]=None, headers:dict[str, str]=None) -> None:
        if end_point is None:
            raise_exception(RequestLayerErrors.URL_EMPTY)
        if params and not type(params) is dict:
            raise_exception(RequestLayerErrors.PARAM_TYPE)
        if params and type(params) is dict and any(not len(param) or not len(params[param]) for param in params):
            raise_exception(RequestLayerErrors.PARAM_LENGTH)
        if headers and not type(headers) is dict:
            raise_exception(RequestLayerErrors.HEADERS_TYPE)
        if headers and type(headers) is dict and any(not len(header) or not len(headers[header]) for header in headers):
            raise_exception(RequestLayerErrors.HEADERS_LENGTH)

    def validate_request_payload(self, end_point:str, data:dict[str, str], params:dict[str, str]=None, headers:dict=None) -> None:
        self.validate_request_data(end_point, params, headers)
        if data and type(data) is not dict:
            raise_exception(RequestLayerErrors.DATA_ERR)