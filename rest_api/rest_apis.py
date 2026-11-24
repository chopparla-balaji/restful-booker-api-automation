from validations.request_layer import RequestLayer
from services.bookings import Bookings
from utils.config_reader import ConfigReader
from typing import Optional
import requests

class RestApis:

    def __init__(self, session:Optional[requests.Session]=None):
        self.session = session if session is not None else requests.Session()
        self.request_layer = RequestLayer()
        self.bookings = Bookings(self.session)

    def get_request(self, end_point:str, params:Optional[dict[str, str]]=None, headers:Optional[dict[str, str]]=None) -> None:
        self.request_layer.validate_request_data(end_point, params, headers)
        self.bookings.get_bookings(ConfigReader.BASE_URL + end_point, params, headers)

    def post_request(self, end_point:str, data:dict[str, str], params:Optional[dict[str, str]]=None, headers:Optional[dict[str, str]]=None) -> None:
        self.request_layer.validate_request_payload(end_point, data, params, headers)
        self.bookings.post_bookings(ConfigReader.BASE_URL + end_point, data, params, headers)

    def update_request(self, end_point:str, data:dict[str, str], params:Optional[dict[str, str]]=None, headers:Optional[dict[str, str]]=None) -> None:
        self.request_layer.validate_request_payload(end_point, data, params, headers)
        self.bookings.update_bookings(ConfigReader.BASE_URL + end_point, data, params, headers)

    def partial_update_request(self, end_point:str, data:dict[str, str], params:Optional[dict[str, str]]=None, headers:Optional[dict[str, str]]=None) -> None:
        self.request_layer.validate_request_payload(end_point, data, params, headers)
        self.bookings.partial_update_bookings(ConfigReader.BASE_URL + end_point, data, params, headers)

    def delete_request(self, end_point:str, params:Optional[dict[str, str]]=None, headers:Optional[dict[str, str]]=None) -> None:
        self.request_layer.validate_request_data(end_point, params, headers)
        self.bookings.delete_bookings(ConfigReader.BASE_URL + end_point, params, headers)
