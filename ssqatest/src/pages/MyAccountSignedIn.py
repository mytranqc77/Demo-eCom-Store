from ssqatest.src.pages.locators.MyAccountSignedInLocator import MyAccountSignedInLocators
from ssqatest.src.SeleniumExtended import SeleniumExtended


class MyAccountSignIn():

    def __init__(self, driver):
        self.driver = driver
        self.selenium = SeleniumExtended(self.driver)

    def verify_user_is_signed_in(self):
        self.selenium.wait_until_element_is_visible(MyAccountSignedInLocators.left_nav_logout_button)

