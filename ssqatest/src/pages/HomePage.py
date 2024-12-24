import time

from ssqatest.src.helpers.config_helpers import get_base_url
from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.pages.locators.HomePageLocator import HomePageLocators


class HomePage(HomePageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.selenium = SeleniumExtended(self.driver)

    def go_to_home_page(self):
        home_url = get_base_url()
        self.driver.get(home_url)

    def click_first_add_to_cart_button(self):
        self.selenium.wait_and_click(self.add_to_cart_button)
        # time.sleep(10)




