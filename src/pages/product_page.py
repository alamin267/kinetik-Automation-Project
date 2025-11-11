from helpers.wait_utils import WaitHelper
from playwright.sync_api import expect
import playwright


class ProductsPage:

    def __init__(self, page, config):
        self.page = page
        self.wait = WaitHelper(page)
        self.base_url = config["base_url"]

        self.product_button = "//a[@href='/products']"
        self.search_button_input_field = "//input[@id='search_product']"
        self.search_button_icon = "//button[@id='submit_search']"
        self.products = "//div[@class='productinfo text-center']"
        self.view_product_button = "a[href='/product_details/1']"

    def check_is_user_navigate_to_all_products_page(self):
        self.wait.wait_for_url_contains("/products")
        print("Navigated to All Products page successfully")

    def enter_product_name_and_search(self, search_item):
        self.wait.wait_and_fill(self.search_button_input_field, search_item)
        self.wait.wait_and_click(self.search_button_icon)
        self.wait.wait_for_page_load()
        print("Entered product name and clicked on the search button")

    def is_searched_product_visible(self, search_item):
        self.wait.wait_for_element_visible(self.products)
        searched_product = self.page.locator(self.products).nth(0)
        product_name = searched_product.locator("xpath=.//p").inner_text().strip()
        if search_item.lower() in product_name.lower():
            print("Search item is visible")
        else:
            print("Search item not found")

    def all_the_search_related_product_are_visible(self):
        self.wait.wait_for_element_visible(self.products)
        count = self.page.locator(self.products).count()
        for i in range(count):
            expect(self.page.locator(self.products).nth(i)).to_be_visible()
        print(f"All search-related products are visible (Total: {count})")







