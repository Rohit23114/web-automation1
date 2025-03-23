from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    def add_to_cart(self, count):
        add_to_cart_btns = self.driver.find_elements(By.CLASS_NAME, "btn_inventory")
        for btn in add_to_cart_btns[:count]:
            btn.click()

    def remove_from_cart(self, count):
        remove_btns = self.driver.find_elements(By.CLASS_NAME, "btn_inventory")
        for btn in remove_btns[:count]:
            btn.click()

    def get_cart_count(self):
        cart_value = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        return int(cart_value.text) if cart_value.text else 0
