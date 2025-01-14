# import time

import pytest
from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.Headers import Headers
from ssqatest.src.pages.CartPage import CartPage


@pytest.mark.usefixtures("init_driver")
class TestEndToEndCheckoutGuestUser:
    @pytest.mark.tc_id33
    def test_end_to_end_checkout_guest_user(self):
        home_page = HomePage(self.driver)
        header = Headers(self.driver)
        cart_page = CartPage(self.driver)
        home_page.go_to_home_page()
        home_page.click_first_add_to_cart_button()

        # Check product is added to basket or not
        header.wait_until_cart_item_count(1)
        header.click_on_cart_on_header()

        # Verify the number of products
        product_names = cart_page.get_products_in_cart()
        assert len(product_names) == 1, f"Expected 1 item in cart but found {len(product_names)}"







