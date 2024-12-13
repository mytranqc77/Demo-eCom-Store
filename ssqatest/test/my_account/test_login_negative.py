import pytest
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut


@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:
    @pytest.mark.tc_id12
    @pytest.mark.smoke
    def test_login_none_existing_user(self):
        print("******")
        print("TEST LOGIN NON EXISTING")
        print("******")
        my_account = MyAccountSignedOut(self.driver)
        my_account.go_to_my_account()
        my_account.input_login_username("mitran")
        my_account.input_login_password("dihdu")
        my_account.click_login_button()

        # expected_error = "ERROR: Invalid username. Lost your password?"
        expected_error = "Error: The username mitran is not registered on this site. " \
                         "If you are unsure of your username, try your email address instead."

        if not my_account.wait_until_error_is_displayed(expected_error):
            Exception("The error message does not match")
