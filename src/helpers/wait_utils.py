from playwright.sync_api import Page, expect, TimeoutError as PlaywrightTimeoutError
import re


class WaitHelper:
    def __init__(self, page: Page):
        self.page = page

    # Wait for element to be visible (throws on timeout)
    def wait_for_element_visible(self, selector: str, timeout: int = 15000):
        self.page.wait_for_selector(selector, state="visible", timeout=timeout)

    # Safe wait for element to be visible (returns True/False)
    def wait_for_element_visible_safe(self, selector: str, timeout: int = 5000) -> bool:
        try:
            self.page.wait_for_selector(selector, state="visible", timeout=timeout)
            return True
        except PlaywrightTimeoutError:
            return False

    #Wait for element to be hidden
    def wait_for_element_hidden(self, selector: str, timeout: int = 15000):
        self.page.wait_for_selector(selector, state="hidden", timeout=timeout)

    # Wait for full page load
    def wait_for_page_load(self, timeout: int = 40000):
        self.page.wait_for_load_state("networkidle", timeout=timeout)

    # Wait for URL to contain text
    def wait_for_url_contains(self, text: str, timeout: int = 15000):
        pattern = re.compile(f".*{re.escape(text)}.*")
        expect(self.page).to_have_url(pattern, timeout=timeout)

    # Wait for text in selector
    def wait_for_text(self, selector: str, text: str, timeout: int = 15000):
        expect(self.page.locator(selector)).to_have_text(text, timeout=timeout)

    # Click after waiting for visibility
    def wait_and_click(self, selector: str, timeout: int = 8000):
        self.wait_for_element_visible(selector, timeout)
        self.page.locator(selector).click()

    # Fill input after waiting for visibility
    def wait_and_fill(self, selector: str, text: str, timeout: int = 8000):
        self.wait_for_element_visible(selector, timeout)
        self.page.locator(selector).fill(text)

    # # Robust page navigation helper
    def goto(self, url: str, timeout: int = 40000, wait_until: str = "networkidle"):
        self.page.goto(url, timeout=timeout, wait_until=wait_until)
        self.wait_for_page_load(timeout)
