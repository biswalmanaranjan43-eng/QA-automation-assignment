"""OrangeHRM login page object."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ALERT = (By.CSS_SELECTOR, ".oxd-alert-content-text")
    REQUIRED_MESSAGES = (By.CSS_SELECTOR, ".oxd-input-field-error-message")

    def open(self, url: str) -> None:
        self.driver.get(url)
        self.wait.until(EC.visibility_of_element_located(self.USERNAME))

    def login(self, username: str, password: str) -> None:
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def submit_empty_form(self) -> None:
        self.click(self.LOGIN_BUTTON)

    def required_messages(self) -> list[str]:
        self.wait.until(lambda driver: len(driver.find_elements(*self.REQUIRED_MESSAGES)) == 2)
        return [message.text for message in self.driver.find_elements(*self.REQUIRED_MESSAGES)]
