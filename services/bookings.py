import requests
from typing import Optional
from validations.response_layer import ResponseLayer

class Bookings:

    def __init__(self, session:Optional[requests.Session]=None):
        self.session = session if session is not None else requests.Session()
        self.response_layer = ResponseLayer()

    def get_bookings(self, full_url:str, params=None, headers=None):
        response = self.session.get(full_url, params=params, headers=headers)
        self.response_layer.validate_response(response)

    def post_bookings(self, full_url:str, data:dict[str, str], params=None, headers=None):
        response = self.session.post(full_url, json=data, params=params, headers=headers)
        self.response_layer.validate_response(response)

    def update_bookings(self, full_url:str, data:dict[str, str], params=None, headers=None):
        response = self.session.put(full_url, json=data, params=params, headers=headers)
        self.response_layer.validate_response(response)

    def partial_update_bookings(self, full_url:str, data:dict[str, str], params=None, headers=None):
        response = self.session.patch(full_url, json=data, params=params, headers=headers)
        self.response_layer.validate_response(response)

    def delete_bookings(self, full_url:str, params=None, headers=None):
        response = self.session.delete(full_url, params=params, headers=headers)
        self.response_layer.validate_response(response)
