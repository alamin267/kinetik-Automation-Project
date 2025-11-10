from playwright.sync_api import Page, expect


class WaitHelper:
    def __init__(self, page: Page):
        self.page = page

    def wait_for_element_visible(self, selector: str, timeout: int = 8000):
        """Wait until an element is visible on the page."""
        self.page.wait_for_selector(selector, state="visible", timeout=timeout)

    def wait_for_element_hidden(self, selector: str, timeout: int = 8000):
        """Wait until an element is hidden or removed."""
        self.page.wait_for_selector(selector, state="hidden", timeout=timeout)

    def wait_for_page_load(self, timeout: int = 15000):
        """Wait until the page is fully loaded (network and DOM)."""
        self.page.wait_for_load_state("networkidle", timeout=timeout)

    def wait_for_url_contains(self, text: str, timeout: int = 10000):
        """
        Wait until the current URL contains the given substring using regex.
        """
        import re
        pattern = re.compile(f".*{re.escape(text)}.*")
        expect(self.page).to_have_url(pattern, timeout=timeout)
        print(f"✅ URL contains '{text}'")

    def wait_for_text(self, selector: str, text: str, timeout: int = 8000):
        """Wait until a specific text appears inside an element."""
        expect(self.page.locator(selector)).to_have_text(text, timeout=timeout)

    def wait_and_click(self, selector: str, timeout: int = 8000):
        """Wait for an element to be visible and then click."""
        self.wait_for_element_visible(selector, timeout)
        self.page.locator(selector).click()

    def wait_and_fill(self, selector: str, text: str, timeout: int = 8000):
        """Wait for input field to be visible and then fill."""
        self.wait_for_element_visible(selector, timeout)
        self.page.locator(selector).fill(text)
