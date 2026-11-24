import requests
from utils.endpoints import Endpoints
from utils.config_reader import ConfigReader
from error_messages.assertion_messages import AssertionMessages

class Authentication:

    def __init__(self):
        ...

    def auth_token(self) -> str :
        request_body:dict[str, str] = {
            "username": ConfigReader.USERNAME,
            "password": ConfigReader.PASSWORD
        }
        headers:dict[str, str] = {
            "Content-Type": "application/json"
        }
        response = requests.post(ConfigReader.BASE_URL + Endpoints.AUTH,
                                 json=request_body,
                                 headers=headers)
        assert response.status_code == 200, AssertionMessages.AUTH_FAILED
        assert response.content, AssertionMessages.RESP_BODY
        response_json = response.json()
        assert "token" in response_json.keys(), AssertionMessages.TOKEN_KEY_MISSING
        assert "token" in response_json.keys() and len(response_json["token"]), AssertionMessages.TOKEN_EMPTY
        return str(response_json["token"])
