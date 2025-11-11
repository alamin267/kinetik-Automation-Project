from helpers.wait_utils import WaitHelper

class ProductDetailPage:

    def __init__(self, page, config):
        self.page = page
        self.wait = WaitHelper(page)
        self.base_url = config["base_url"]

        # Locators
        self.write_your_review_text = "//a[normalize-space()='Write Your Review']"
        self.quantity_button = "//input[@id='quantity']"
        self.add_to_cart_button = "//button[normalize-space()='Add to cart']"
        self.view_cart_button = "//u[normalize-space()='View Cart']"

    def is_product_detail_visible(self):
        self.wait.wait_for_element_visible(self.write_your_review_text)
        print("Product Details are visible")

    def set_product_quantity_and_add_to_cart_product(self, quantity):
        self.wait.wait_and_fill(self.quantity_button, quantity)
        self.wait.wait_and_click(self.add_to_cart_button)
        self.wait.wait_and_click(self.view_cart_button)
        print("Product added to cart successfully")

    def increase_product_quantity(self):
        self.wait.wait_for_element_visible(self.quantity_button)
        self.page.locator(self.quantity_button).click()
        for _ in range(3):
            self.page.locator(self.quantity_button).press("ArrowUp")
        print("Product quantity increased")

    def addToCart_button_click(self):
        self.wait.wait_and_click(self.add_to_cart_button)
        print("Add to cart button clicked")

    def view_cart_button_click(self):
        self.wait.wait_and_click(self.view_cart_button)
        print("View cart button clicked")
