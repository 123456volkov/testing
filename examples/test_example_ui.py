import os
import pytest

from framework.ui.base_ui_test import UIDriver

pytestmark = pytest.mark.skipif(
    not os.environ.get("ENABLE_UI_TESTS"),
    reason="UI tests are disabled; set ENABLE_UI_TESTS to enable"
)


def test_open_example() -> None:
    driver = UIDriver()
    if driver.driver is None:
        pytest.skip("WebDriver not available")
    driver.open("https://example.com")
    assert "Example Domain" in driver.driver.title
    driver.quit()
