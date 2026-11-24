import requests
from utils.exceptions import raise_exception
from error_messages.response_layer_errors import ResponseLayerErrors

class ResponseLayer:

    def validate_response(self, response:requests.Response):
        if response.status_code != 200:
            raise_exception(ResponseLayerErrors.STATUS_CODE.format(response.status_code))
