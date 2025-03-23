from selenium.webdriver.common.by import By
from time import sleep

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_url(self, url):
        self.driver.get(url)
        sleep(3)  # Use implicit waits in production code
