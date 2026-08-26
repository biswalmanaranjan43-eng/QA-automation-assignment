import pytest

from api.orangehrm_client import OrangeHrmClient
from config.settings import settings


@pytest.mark.api
def test_api_001_authenticated_employee_list_returns_key_fields(api_client):
    login_response = api_client.login(settings.username, settings.password)
    assert login_response.status_code == 302
    assert "/dashboard" in login_response.headers["Location"]

    response = api_client.list_employees(limit=10)
    assert response.status_code == 200
    body = response.json()
    assert isinstance(body["data"], list)
    assert isinstance(body["meta"], dict)


@pytest.mark.api
def test_api_002_unauthenticated_employee_list_is_rejected():
    client = OrangeHrmClient(settings.web_url, settings.api_url, settings.timeout_seconds)
    try:
        response = client.list_employees(limit=10)
    finally:
        client.close()

    assert response.status_code == 401
    assert response.headers["Content-Type"].startswith("application/json")


@pytest.mark.api
def test_api_003_invalid_credentials_do_not_create_an_authenticated_session(api_client):
    response = api_client.login("invalid-user", "invalid-password")
    assert response.status_code == 302
    assert "/auth/login" in response.headers["Location"]

    protected_response = api_client.list_employees(limit=1)
    assert protected_response.status_code == 401
