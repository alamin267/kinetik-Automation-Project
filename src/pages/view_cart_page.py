import time
import re
from playwright.sync_api import expect

class ViewCartPage:

    def __init__(self, page):
        self.page = page
        self.url="https://automationexercise.com/"

        #Locators
        self.cart_page_url = "https://automationexercise.com/view_cart"
        #self.page.wait_for_selector("//button[normalize-space()='4']", timeout=20000)
        self.check_quantity = page.locator("//td[@class='cart_quantity']/button")


    def check_view_cart_page_and_product_quantity(self, product_quantity):
        time.sleep(5)
        assert "/view_cart" in self.page.url, "User is not navigated to View Cart page"
        print("Product displayed view cart page")

        #expect(self.check_quantity).to_be_visible()
        quantity = self.check_quantity.inner_text()
        if quantity == product_quantity:
            print("Quantity match is the view cart page")
        else:
            print("Quantity doesn't match is the view cart page")
            return




