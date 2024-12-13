from selenium.webdriver.common.by import By


class MyAccountSignedInLocators:
    left_nav_logout_button = (By.CSS_SELECTOR,
                              'li.woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout')