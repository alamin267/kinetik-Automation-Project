import time
from urllib.parse import quote

from pages.home_page import HomePage
from pages.product_page import ProductsPage
from utils.data_loader import load_test_data


def test_home_page(page):
    data = load_test_data("products.json")
    search_term = data["search_product"]

    home_page = HomePage(page)
    product_page = ProductsPage(page)

    home_page.visit_home_page()
    home_page.is_homePage_visible()
    home_page.is_homePage_visible()
    home_page.click_product_button()
    product_page.check_is_user_navigate_to_all_products_page()
    product_page.enter_product_name_and_search(search_term)
    product_page.is_searched_product_visible(search_term)
    product_page.all_the_search_related_product_are_visible()
    time.sleep(5)

