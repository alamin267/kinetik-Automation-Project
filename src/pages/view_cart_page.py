from helpers.wait_utils import WaitHelper
from playwright.sync_api import expect


class ViewCartPage:

    def __init__(self, page, config):
        self.page = page
        self.wait = WaitHelper(page)  # Initialize the helper
        self.base_url = config["base_url"]

        # Locators
        self.cart_page_url = "/view_cart"
        self.check_quantity = "//td[@class='cart_quantity']/button"

    def check_view_cart_page_and_product_quantity(self, product_quantity):
        # Wait until the URL contains '/view_cart'
        self.wait.wait_for_url_contains(self.cart_page_url)
        print("User is on the View Cart page")

        self.wait.wait_for_element_visible(self.check_quantity)

        # Check quantity
        quantity_text = self.page.locator(self.check_quantity).inner_text().strip()
        if quantity_text == product_quantity:
            print(f"Quantity matches on View Cart page: {quantity_text}")
        else:
            print(f"Quantity does NOT match on View Cart page. Expected: {product_quantity}, Found: {quantity_text}")
            return
