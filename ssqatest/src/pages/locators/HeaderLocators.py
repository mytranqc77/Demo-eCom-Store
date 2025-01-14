
from selenium.webdriver.common.by import By


class HeaderLocators:

    cart_on_the_right_side = (By.ID, 'site-header-cart')
    item_count = (By.CSS_SELECTOR, 'ul#site-header-cart span.count')

