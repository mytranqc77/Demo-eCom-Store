import logging

from ssqatest.src.pages.locators.MyAccountSignedOutLocator import MyAccountSignedOutLocator
from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.helpers.config_helpers import get_base_url
import logging as logger
from selenium import webdriver
import time

# logger.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s",
#     handlers=[
#         logging.StreamHandler(),
#         logging.FileHandler("my_account_logs.log"),
#     ]
# )


class MyAccountSignedOut(MyAccountSignedOutLocator):
    endpoint = "/my-account/"

    def __init__(self, driver):
        self.driver = driver  # Save the driver for later use
        self.selenium = SeleniumExtended(self.driver)  # Pass it to SeleniumExtended

    def go_to_my_account(self):
        my_account_url = get_base_url() + self.endpoint
        logger.info(f"Going to: {my_account_url}")
        self.driver.get(my_account_url)

    def input_login_username(self, username):
        self.selenium.wait_and_input_text(MyAccountSignedOutLocator.login_username, username)

    def input_login_password(self, password):
        self.selenium.wait_and_input_text(MyAccountSignedOutLocator.login_password, password)

    def click_login_button(self):
        logger.debug("Clicking 'login' button")
        self.selenium.wait_and_click(MyAccountSignedOutLocator.login_button)

    def wait_until_error_is_displayed(self, exp_error):
        self.selenium.wait_until_element_contains_text(MyAccountSignedOutLocator.errors_ul, exp_error)

    def input_register_username(self, username):
        self.selenium.wait_and_input_text(MyAccountSignedOutLocator.register_email, username)

    def input_register_password(self, password):
        self.selenium.wait_and_input_text(MyAccountSignedOutLocator.register_password, password)

    def click_register_button(self):
        logger.debug("Clicking 'login' button")
        self.selenium.wait_and_click(MyAccountSignedOutLocator.register_button)









