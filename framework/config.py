from __future__ import annotations

from dataclasses import dataclass
import os


@dataclass
class AppConfig:
    """Configuration for tests.

    Values are taken from environment variables if present so the framework can
    be configured without modifying code.
    """

    base_url: str = os.getenv("BASE_URL", "https://example.com")
    api_base_url: str = os.getenv("API_BASE_URL", "https://httpbin.org")
    headless: bool = os.getenv("HEADLESS", "true").lower() == "true"

