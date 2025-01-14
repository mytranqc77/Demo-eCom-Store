import time

from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.pages.locators.HeaderLocators import HeaderLocators


class Headers(HeaderLocators):

    def __init__(self, driver):
        self.driver = driver
        self.selenium = SeleniumExtended(self.driver)

    def click_on_cart_on_header(self):
        self.selenium.wait_and_click(self.cart_on_the_right_side)

    def wait_until_cart_item_count(self, count):
        self.expected_item_count = str(count) + ' item'
        self.selenium.wait_until_element_contains_text(self.item_count, self.expected_item_count)


