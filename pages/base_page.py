"""Shared Selenium actions implemented with explicit waits only."""

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver, timeout: int) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click(self, locator: tuple[str, str]) -> None:
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator: tuple[str, str], value: str) -> None:
        field = self.wait.until(EC.visibility_of_element_located(locator))
        field.clear()
        field.send_keys(value)

    def visible_text(self, locator: tuple[str, str]) -> str:
        return self.wait.until(EC.visibility_of_element_located(locator)).text
