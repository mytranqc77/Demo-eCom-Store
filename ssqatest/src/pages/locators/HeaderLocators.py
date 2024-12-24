
from selenium.webdriver.common.by import By
from ssqatest.src.pages.Headers import Headers


class HeaderLocators(Headers):

    cart = (By.CSS_SELECTOR, '#site-navigation > div:nth-child(2) > ul > li.page_item.page-item-7 > a')
    item_count = (By.CSS_SELECTOR, '#site-header-cart > li:nth-child(1) > a > span.count')

