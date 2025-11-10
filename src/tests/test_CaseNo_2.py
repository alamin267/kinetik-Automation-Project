import time
from urllib.parse import quote
from pages.home_page import HomePage
from pages.product_details_page import ProductDetailPage
from pages.view_cart_page import ViewCartPage
from utils.data_loader import load_test_data


def test_case_no_2(page, config):

    data = load_test_data("products.json")
    quantity = data["product_quantity"]
    home_page = HomePage(page, config)
    product_detail_page = ProductDetailPage(page, config)
    view_cart_page = ViewCartPage(page, config)

    home_page.visit_home_page()
    home_page.is_homePage_visible()
    home_page.click_view_product_button()
    product_detail_page.is_product_detail_visible()
    product_detail_page.increase_product_quantity()
    product_detail_page.addToCart_button_click()
    product_detail_page.view_cart_button_click()
    view_cart_page.check_view_cart_page_and_product_quantity(quantity)



