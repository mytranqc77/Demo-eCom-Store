from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.pages.locators.CartPageLocator import CartPageLocator


class CartPage(CartPageLocator):

    def __init__(self, driver):
        self.driver = driver
        self.selenium = SeleniumExtended(self.driver)

    def get_products_in_cart(self):
        product_name_elements = self.selenium.wait_and_get_elements(self.products_in_cart)
        product_names = [i.text for i in product_name_elements]
        print(product_names)
        return product_names

    def enter_coupon(self, coupon_code):
        self.selenium.wait_and_input_text(self.coupon_code_field, coupon_code)

    def click_apply_coupon(self):
        self.selenium.wait_and_click(self.apply_coupon_button)

    def apply_coupon(self, coupon_code):
        self.enter_coupon(coupon_code)
        self.click_apply_coupon()
        actual_message = self.get_displayed_message()
        assert actual_message == "Coupon code applied successfully.", \
            "Message does not match"

    def get_displayed_message(self):
        success_message = self.selenium.wait_and_get_text(self.cart_page_message)
        return success_message












