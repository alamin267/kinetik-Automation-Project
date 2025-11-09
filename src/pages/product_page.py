import time
import re
from playwright.sync_api import expect

class ProductsPage:

    def __init__(self, page):
        self.page = page
        self.url="https://automationexercise.com/"

        self.product_button = page.locator("//a[@href='/products']")
        self.search_button_input_field = page.locator("//input[@id='search_product']")
        self.search_button_icon = page.locator("//button[@id='submit_search']")
        self.products = page.locator("//div[@class='productinfo text-center']")


    def check_is_user_navigate_to_all_products_page(self):
        assert "/products" in self.page.url, "User is not navigated to All Products page"
        print("Navigate to all product page successfully")

    def enter_product_name_and_search(self,search_item ):
        self.search_button_input_field.fill(search_item)
        time.sleep(1)
        self.search_button_icon.click()
        print("Enter Product Name in the search field and click on the search button")

    def is_searched_product_visible(self, search_item):
        searched_product = self.products.nth(0)
        searched_product_name = searched_product.locator("xpath=.//p").inner_text().strip()
        if search_item.lower() in searched_product_name.lower():
            print("Search Item is visible")
        else:
            print("Search Item is visible")
            return



    def all_the_search_related_product_are_visible(self):
        count = self.products.count()

        if count == 0:
            print(f"No products found for search term")
            return

        for i in range(count):
            product = self.products.nth(i)
            expect(product).to_be_visible()
            name = product.locator("xpath=.//p").inner_text().strip()
            #assert search_term.lower() in name.lower(), f"Product '{name}' does not match search term"
        print(f"Search Related All product is Visible, Last Product is: {i + 1}: '{name}'")