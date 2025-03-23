import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from utils.driver_factory import create_driver

def test_login_successful():
    driver = create_driver()
    login_page = LoginPage(driver)
    login_page.go_to_login_page()
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_logged_in()
    driver.quit()
