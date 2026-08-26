"""OrangeHRM dashboard page object."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class DashboardPage(BasePage):
    HEADER = (By.CSS_SELECTOR, "h6.oxd-topbar-header-breadcrumb-module")

    def wait_until_loaded(self) -> None:
        self.wait.until(EC.url_contains("/dashboard"))
        self.wait.until(EC.text_to_be_present_in_element(self.HEADER, "Dashboard"))
