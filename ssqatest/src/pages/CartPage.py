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


