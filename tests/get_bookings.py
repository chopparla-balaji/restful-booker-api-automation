from rest_api.rest_apis import RestApis
from utils.endpoints import Endpoints

class TestGetBookings:

    def test_get_bookings(self, auth_session):
        api = RestApis(auth_session)
        api.get_request(end_point=Endpoints.BOOKINGS)
