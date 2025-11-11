from playwright.sync_api import Page, expect


class WaitHelper:
    def __init__(self, page: Page):
        self.page = page

    def wait_for_element_visible(self, selector: str, timeout: int = 8000):
        self.page.wait_for_selector(selector, state="visible", timeout=timeout)

    def wait_for_element_hidden(self, selector: str, timeout: int = 8000):
        self.page.wait_for_selector(selector, state="hidden", timeout=timeout)

    def wait_for_page_load(self, timeout: int = 15000):
        self.page.wait_for_load_state("networkidle", timeout=timeout)

    def wait_for_url_contains(self, text: str, timeout: int = 10000):
        import re
        pattern = re.compile(f".*{re.escape(text)}.*")
        expect(self.page).to_have_url(pattern, timeout=timeout)

    def wait_for_text(self, selector: str, text: str, timeout: int = 8000):
        expect(self.page.locator(selector)).to_have_text(text, timeout=timeout)

    def wait_and_click(self, selector: str, timeout: int = 8000):
        self.wait_for_element_visible(selector, timeout)
        self.page.locator(selector).click()

    def wait_and_fill(self, selector: str, text: str, timeout: int = 8000):
        self.wait_for_element_visible(selector, timeout)
        self.page.locator(selector).fill(text)
