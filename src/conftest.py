import pytest
from playwright.sync_api import sync_playwright
import allure
import os
import yaml


# ---------------- CONFIGURATION LOADER ----------------
def load_config(env="qa"):
    """Load environment settings from YAML config file."""
    config_path = os.path.join(os.path.dirname(__file__), "config", "config.yaml")
    with open(config_path, "r") as f:
        data = yaml.safe_load(f)
    return data.get(env)


@pytest.fixture(scope="session")
def config(pytestconfig):
    """Fixture to provide environment config."""
    env = pytestconfig.getoption("--env") or "qa"
    return load_config(env)


# ---------------- PLAYWRIGHT FIXTURES ----------------
@pytest.fixture(scope="session")
def browser(config):
    """Launch browser session based on config settings."""
    with sync_playwright() as p:
        browser_type = getattr(p, config["browser"])  # chromium / firefox / webkit
        browser = browser_type.launch(
            headless=config["headless"],
            args=["--window-size=1920,1080"]
        )
        yield browser
        browser.close()


@pytest.fixture
def page(browser, config):
    """Create a new isolated browser context for each test."""
    context = browser.new_context(base_url=config["base_url"], viewport=None)
    page = context.new_page()
    yield page
    context.close()


# ---------------- ALLURE REPORTING ----------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """Attach screenshot to Allure report on test failure."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page", None)
        if page:
            screenshot_dir = "reports/screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"{item.name}.png")

            page.screenshot(path=screenshot_path)
            allure.attach.file(
                screenshot_path,
                name=f"Screenshot - {item.name}",
                attachment_type=allure.attachment_type.PNG
            )


# ---------------- CLI OPTIONS ----------------
def pytest_addoption(parser):
    """Allow selecting environment via CLI."""
    parser.addoption("--env", action="store", default="qa", help="Environment: qa / staging / prod")