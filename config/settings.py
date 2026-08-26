"""Centralised, environment-overridable configuration."""

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    base_url: str = os.getenv("ORANGEHRM_BASE_URL", "https://opensource-demo.orangehrmlive.com")
    username: str = os.getenv("ORANGEHRM_USERNAME", "Admin")
    password: str = os.getenv("ORANGEHRM_PASSWORD", "admin123")
    timeout_seconds: int = int(os.getenv("ORANGEHRM_TIMEOUT", "15"))
    headless: bool = os.getenv("HEADLESS", "true").lower() == "true"

    @property
    def web_url(self) -> str:
        return f"{self.base_url.rstrip('/')}/web/index.php"

    @property
    def login_url(self) -> str:
        return f"{self.web_url}/auth/login"

    @property
    def api_url(self) -> str:
        return f"{self.web_url}/api/v2"


settings = Settings()
