from selenium.webdriver.common.by import By


class OrderReceivedPageLocators:
    Page_main_header = (By.CSS_SELECTOR, 'header h1.entry-title')
    order_number = (By.CSS_SELECTOR, 'li.order strong')

