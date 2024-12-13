from selenium.webdriver.common.by import By


class MyAccountSignedOutLocator:
    login_username = (By.ID, 'username')
    login_password = (By.ID, 'password')
    login_button = (By.CSS_SELECTOR, 'button[value="Log in"]')
    errors_ul = (By.CSS_SELECTOR, '#content > div > div.woocommerce > ul > li')
    register_email = (By.ID, 'reg_email')
    register_password = (By.CSS_SELECTOR, '#reg_password')
    register_button = (By.CSS_SELECTOR, '#customer_login > div.u-column2.col-2 > form > p:nth-child(4) > button')

