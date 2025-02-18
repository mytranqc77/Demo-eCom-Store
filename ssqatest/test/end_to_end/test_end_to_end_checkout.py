# import time

import pytest
from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.Headers import Headers
from ssqatest.src.pages.CartPage import CartPage
from ssqatest.src.pages.CheckoutPage import CheckoutPage
from ssqatest.src.pages.OrderReceivedPage import OrderReceivedPage
from ssqatest.src.configs.generic_configs import GenericConfigs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging as logger


@pytest.mark.usefixtures("init_driver")
class TestEndToEndCheckoutGuestUser:
    @pytest.mark.tc_id33
    def test_end_to_end_checkout_guest_user(self):
        home_page = HomePage(self.driver)
        header = Headers(self.driver)
        cart_page = CartPage(self.driver)
        home_page.go_to_home_page()
        home_page.click_first_add_to_cart_button()
        checkout_page = CheckoutPage(self.driver)
        order_received_page = OrderReceivedPage(self.driver)

        # Check product is added to basket or not
        header.wait_until_cart_item_count(1)
        header.click_on_cart_on_header()

        # Verify the number of products
        product_names = cart_page.get_products_in_cart()
        assert len(product_names) == 1, f"Expected 1 item in cart but found {len(product_names)}"

        # apply free coupon
        coupon_code = GenericConfigs.free_coupon
        cart_page.apply_coupon(coupon_code)

        # click check out button
        cart_page.click_checkout_button()

        # Filling in billing info:
        checkout_page.fill_in_billing_info()

        # Proceed to checkout
        checkout_page.check_out()
        # import pdb; pdb.set_trace()

        # Verify order received:
        order_received_page.verify_order_received()

        # Verify order number:
        order_number = order_received_page.verify_order_number()
        print(f"The order number is: {order_number}")














