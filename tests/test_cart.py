import pytest
from pages.cart_page import CartPage
from utils.driver_factory import create_driver

def test_add_to_cart():
    driver = create_driver()
    cart_page = CartPage(driver)
    cart_page.add_to_cart(3)  # Add 3 items to the cart
    assert cart_page.get_cart_count() == 3
    driver.quit()

def test_remove_from_cart():
    driver = create_driver()
    cart_page = CartPage(driver)
    cart_page.add_to_cart(3)
    cart_page.remove_from_cart(2)  # Remove 2 items from the cart
    assert cart_page.get_cart_count() == 1
    driver.quit()
