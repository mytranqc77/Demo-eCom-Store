from selenium.webdriver.common.by import By


class CartPageLocator:
    products_in_cart = (By.CSS_SELECTOR, 'tr.cart_item td.product-name')
