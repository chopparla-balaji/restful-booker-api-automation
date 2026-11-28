from rest_api.rest_apis import RestApis
from utils.endpoints import Endpoints
from utils.exceptions import raise_exception
from error_messages.test_layer_errors import TestLayerErrors

class TestGetBookings:

    responseType = dict

    def test_get_bookings(self, auth_session):
        api = RestApis(auth_session)
        response = api.get_request(end_point=Endpoints.BOOKINGS)
        if not type(response) == self.responseType:
            raise_exception(TestLayerErrors.RESP_TYPE_NOT_MATCH)
