import time
import re
from playwright.sync_api import expect


class HomePage:

    def __init__(self, page):
        self.page = page
        self.url = "https://automationexercise.com/"

        # Locators
        self.home_page_logo = page.locator("//img[@alt='Website for automation practice']")
        self.product_button = page.locator("//a[@href='/products']")
        self.view_product_button = page.locator("a[href='/product_details/1']")

    def visit_home_page(self):
        self.page.goto(self.url, timeout=60000)
        self.page.set_viewport_size({"width": 1920, "height": 1080})
        time.sleep(1)

    def is_homePage_visible(self):
        if self.home_page_logo.is_visible():
            print("\nHome page visible")
        else:
            print("Home page NOT visible")

    def click_product_button(self):
        self.product_button.click()
        print("Click on the product button")
        time.sleep(2)

    def click_view_product_button(self):
        self.view_product_button.click()
        print("View Product button is clicked")
        time.sleep(2)
