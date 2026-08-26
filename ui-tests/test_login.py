import pytest

from config.settings import settings
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


@pytest.mark.ui
def test_ui_001_valid_admin_login_opens_dashboard(driver):
    login_page = LoginPage(driver, settings.timeout_seconds)
    login_page.open(settings.login_url)
    login_page.login(settings.username, settings.password)

    dashboard = DashboardPage(driver, settings.timeout_seconds)
    dashboard.wait_until_loaded()
    assert "/dashboard" in driver.current_url


@pytest.mark.ui
def test_ui_003_invalid_password_shows_credentials_error(driver):
    login_page = LoginPage(driver, settings.timeout_seconds)
    login_page.open(settings.login_url)
    login_page.login(settings.username, "incorrect-password")

    assert login_page.visible_text(login_page.ALERT) == "Invalid credentials"


@pytest.mark.ui
def test_ui_004_empty_login_shows_required_errors(driver):
    login_page = LoginPage(driver, settings.timeout_seconds)
    login_page.open(settings.login_url)
    login_page.submit_empty_form()

    assert login_page.required_messages() == ["Required", "Required"]
