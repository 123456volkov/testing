from __future__ import annotations

from typing import Optional

from ..config import AppConfig
from ..utils.logger import get_logger

try:  # pragma: no cover - optional dependency
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
except Exception:  # pragma: no cover - optional dependency
    webdriver = None  # type: ignore
    Options = None  # type: ignore


class UIDriver:
    """Wrapper around Selenium WebDriver for UI testing."""

    def __init__(self, config: Optional[AppConfig] = None) -> None:
        self.config = config or AppConfig()
        self.logger = get_logger(self.__class__.__name__)
        self.driver = None
        if webdriver is None:
            self.logger.warning("Selenium is not available; UI tests will be skipped")
            return
        options = Options()
        if self.config.headless:
            options.add_argument("--headless=new")
        try:
            self.driver = webdriver.Chrome(options=options)
        except Exception as exc:  # pragma: no cover - environment dependent
            self.logger.warning("Could not start Chrome driver: %s", exc)
            self.driver = None

    def open(self, url: str) -> None:
        if not self.driver:
            raise RuntimeError("WebDriver is not available")
        self.logger.info("OPEN %s", url)
        self.driver.get(url)

    def quit(self) -> None:
        if self.driver:
            self.driver.quit()
            self.driver = None
