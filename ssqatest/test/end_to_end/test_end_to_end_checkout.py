# import time

import pytest
from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.Headers import Headers


@pytest.mark.usefixtures("init_driver")
class TestEndToEndCheckoutGuestUser:
    @pytest.mark.tc_id33
    def test_end_to_end_checkout_guest_user(self):
        home_page = HomePage(self.driver)
        header = Headers(self.driver)
        home_page.go_to_home_page()
        home_page.click_first_add_to_cart_button()

        # Check product is added to basket or not
        header.check_item(1)
        header.click_on_cart_on_header()
