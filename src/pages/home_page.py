from helpers.wait_utils import WaitHelper
from playwright.sync_api import expect


class HomePage:

    def __init__(self, page, config):
        self.page = page
        self.wait = WaitHelper(page)
        self.base_url = config["base_url"]

        # Locators
        self.home_page_logo = "//img[@alt='Website for automation practice']"
        self.product_button = "//a[@href='/products']"
        self.view_product_button = "a[href='/product_details/1']"

    def visit_home_page(self):
        self.page.goto(self.base_url)
        self.page.set_viewport_size({"width": 1900, "height": 1080})
        self.wait.wait_for_page_load()
        self.wait.wait_for_element_visible(self.home_page_logo)

    def is_homePage_visible(self):
        if self.page.locator(self.home_page_logo).is_visible():
            print("\nHome page visible")
        else:
            print("Home page NOT visible")

    def click_product_button(self):
        self.wait.wait_and_click(self.product_button)
        self.wait.wait_for_page_load()
        print("Clicked on the product button")

    def click_view_product_button(self):
        self.wait.wait_and_click(self.view_product_button)
        self.wait.wait_for_page_load()
        print("View Product button is clicked")
