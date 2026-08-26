"""Shared pytest fixtures for UI and API tests."""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from api.orangehrm_client import OrangeHrmClient
from config.settings import settings


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--headed", action="store_true", help="Run UI tests with a visible browser.")


@pytest.fixture
def driver(request: pytest.FixtureRequest):
    options = Options()
    if settings.headless and not request.config.getoption("--headed"):
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1440,1000")
    options.add_argument("--disable-notifications")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


@pytest.fixture
def api_client() -> OrangeHrmClient:
    client = OrangeHrmClient(settings.web_url, settings.api_url, settings.timeout_seconds)
    yield client
    client.close()
