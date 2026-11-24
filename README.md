# Restful Booker API Automation

A layered REST API test automation framework built with **Python**, **Pytest**, and **Requests**, targeting the [Restful Booker](https://restful-booker.herokuapp.com/) API. It covers authentication and CRUD operations with a clean separation between the test, service, request-validation, and response-validation layers.

## Features

- **Layered architecture** — tests, API orchestration, services, and validation are decoupled
- **Session-based authentication** — logs in once per run and reuses an authenticated `requests.Session`
- **Reusable Pytest fixtures** — shared authenticated session via `conftest.py`
- **Request validation** — endpoint, params, headers, and payload checked before the call
- **Response validation** — centralized status-code assertion
- **Externalized configuration** — base URL and credentials loaded from an env file
- **Centralized error messages** — assertion and validation messages kept in one place

## Tech Stack

| Purpose        | Tool              |
| -------------- | ----------------- |
| Language       | Python 3.11+      |
| Test runner    | Pytest            |
| HTTP client    | Requests          |
| Config loading | python-dotenv     |

## Project Structure

```
restful-booker-api-automation/
├── authentication/      # Auth flow – fetches the API token
├── rest_api/            # RestApis – orchestrates validation + service calls
├── services/            # Bookings – HTTP calls via a shared session
├── validations/         # Request & response validation layers
├── error_messages/      # Centralized assertion / error strings
├── utils/               # Config reader, endpoints, exceptions
├── tests/               # Pytest test cases
├── conftest.py          # Shared fixtures (authenticated session)
└── environments.env     # Base URL + credentials (not committed)
```

## Getting Started

### Prerequisites
- Python 3.11 or higher

### Installation

```bash
git clone https://github.com/chopparla-balaji/restful-booker-api-automation.git
cd restful-booker-api-automation
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
pip install -r requirements.txt
```

### Configuration

Create an `environments.env` file in the project root (use `environments.env.example` as a template):

```env
BASE_URL=https://restful-booker.herokuapp.com
USERNAME=admin
PASSWORD=password123
```

## Running the Tests

```bash
# Run all tests
pytest

# Verbose output
pytest -v

# Run a specific test file
pytest tests/get_bookings.py
```

## How It Works

1. The `auth_session` fixture (`conftest.py`) logs in once and stores the token on a `requests.Session`.
2. Tests pass that session into `RestApis`, which runs request validation and delegates to `Bookings`.
3. `Bookings` makes the HTTP call through the shared session (the token is sent automatically).
4. `ResponseLayer` validates the response.

```
test → RestApis → RequestLayer (validate) → Bookings (session.get/post/...) → ResponseLayer (validate)
```

## Roadmap

- [ ] Return the response body so tests can assert on data, not just status
- [ ] Configurable expected status codes per request (e.g. 201 for DELETE)
- [ ] Full CRUD test coverage with positive and negative scenarios
- [ ] Data-driven testing
- [ ] Logging
- [ ] HTML test reports (pytest-html / Allure)
- [ ] CI integration (GitHub Actions)
```
