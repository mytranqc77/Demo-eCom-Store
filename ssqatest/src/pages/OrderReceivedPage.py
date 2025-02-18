from ssqatest.src.pages.locators.OrderReceivedPageLocators import OrderReceivedPageLocators
from ssqatest.src.SeleniumExtended import SeleniumExtended


class OrderReceivedPage(OrderReceivedPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.selenium = SeleniumExtended(driver)

    def verify_order_received(self):
        self.selenium.wait_until_element_contains_text(self.Page_main_header, "Order received")

    def verify_order_number(self):
        order_number = self.selenium.wait_and_get_text(self.order_number)
        return order_number






