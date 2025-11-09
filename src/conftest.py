import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--window-size=1920,1080"])
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context(viewport=None)
    page = context.new_page()
    yield page
    context.close()