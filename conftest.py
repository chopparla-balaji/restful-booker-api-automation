import pytest
import requests
from authentication.authentication import Authentication


@pytest.fixture(scope="session")
def auth_session():
    """Logs in once per test run and returns a requests.Session that
    carries the auth token (as a cookie) on every request made through it."""
    session = requests.Session()
    token = Authentication().auth_token()
    session.cookies.set("token", token)
    yield session
    session.close()
