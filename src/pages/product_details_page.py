import time
import re


class ProductDetailPage:

    def __init__(self, page):
        self.page = page
        self.url="https://automationexercise.com/"

       #Locators
        self.write_your_review_text = page.locator("//a[normalize-space()='Write Your Review']")
        self.quantity_button = page.locator("//input[@id='quantity']")
        self.add_to_cart_button = page.locator("//button[normalize-space()='Add to cart']")
        self.view_cart_button = page.locator("//u[normalize-space()='View Cart']")



    def is_product_detail_visible(self):
        if self.write_your_review_text.is_visible():
            print("Product Details is opened")
        else:
            print("Product Details is not visible")

    def set_product_quantity_and_add_to_cart_product(self, quantity):
        self.quantity_button.fill(quantity)
        time.sleep(2)
        self.add_to_cart_button.click()
        self.view_cart_button.click()
        time.sleep(2)

    def increase_product_quantity(self):
        self.quantity_button.click()
        for _ in range(3):
            self.quantity_button.press("ArrowUp")

        print("Product Quantity increased")

    def addToCart_button_click(self):
        self.add_to_cart_button.click()
        print("Add to cart button is clicked")

    def view_cart_button_click(self):
        self.view_cart_button.click()
        print("View cart button is clicked")

