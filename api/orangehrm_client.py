"""Session-based client for the OrangeHRM demo's internal REST endpoints."""

from html.parser import HTMLParser

import requests


class _CsrfTokenParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.token: str | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "input":
            return
        attributes = dict(attrs)
        if attributes.get("name") == "_token":
            self.token = attributes.get("value")


class OrangeHrmClient:
    def __init__(self, web_url: str, api_url: str, timeout: int) -> None:
        self.web_url = web_url.rstrip("/")
        self.api_url = api_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()

    def close(self) -> None:
        self.session.close()

    def login(self, username: str, password: str) -> requests.Response:
        login_url = f"{self.web_url}/auth/login"
        login_page = self.session.get(login_url, timeout=self.timeout)
        login_page.raise_for_status()

        parser = _CsrfTokenParser()
        parser.feed(login_page.text)
        if not parser.token:
            raise RuntimeError("OrangeHRM login page did not include a CSRF token.")

        return self.session.post(
            f"{self.web_url}/auth/validate",
            data={"_token": parser.token, "username": username, "password": password},
            headers={"Referer": login_url},
            allow_redirects=False,
            timeout=self.timeout,
        )

    def list_employees(self, limit: int = 1, offset: int = 0) -> requests.Response:
        return self.session.get(
            f"{self.api_url}/pim/employees",
            params={"limit": limit, "offset": offset},
            timeout=self.timeout,
        )
