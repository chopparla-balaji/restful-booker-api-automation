import requests
from utils.exceptions import raise_exception
from utils.status_codes import StatusCodes
from error_messages.response_layer_errors import ResponseLayerErrors

class ResponseLayer:

    def validate_response(self, response:requests.Response):
        expected_code = int(StatusCodes.STATUS_CODES[response.request.method])
        if response.status_code != expected_code:
            raise_exception(ResponseLayerErrors.STATUS_CODE.format(response.status_code))
        request_content_type = response.request.headers.get('Content-Type', '').split(';')[0]
        response_content_type = response.headers.get('Content-Type', '').split(';')[0]
        if request_content_type and response_content_type and request_content_type != response_content_type:
            raise_exception(ResponseLayerErrors.CONTENT_TYPE_NOT_MATCH)
