
from selenium.webdriver.common.by import By


class HeaderLocators:

    cart = (By.CSS_SELECTOR, '#site-navigation > div:nth-child(2) > ul > li.page_item.page-item-7 > a')
    item_count = (By.CSS_SELECTOR, 'ul#site-header-cart span.count')

