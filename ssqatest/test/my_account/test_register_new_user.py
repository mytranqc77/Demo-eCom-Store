import pdb

import pytest
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut
from ssqatest.src.pages.MyAccountSignedIn import MyAccountSignIn
from ssqatest.src.helpers.generic_helpers import generate_random_email_and_password


@pytest.mark.usefixtures("init_driver")
class TestRegisterNewUser:

    @pytest.mark.tc_id13
    def test_register_valid_new_user(self):
        access_my_account = MyAccountSignedOut(self.driver)
        my_account_sign_in = MyAccountSignIn(self.driver)
        access_my_account.go_to_my_account()
        random_test_account = generate_random_email_and_password()
        print(random_test_account["Email"])
        print(random_test_account["Password"])
        access_my_account.input_register_username(random_test_account["Email"])
        access_my_account.input_register_password(random_test_account["Password"])
        access_my_account.click_register_button()

        # Verify user is registered
        my_account_sign_in.verify_user_is_signed_in()


