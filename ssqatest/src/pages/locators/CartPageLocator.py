from selenium.webdriver.common.by import By


class CartPageLocator:
    products_in_cart = (By.CSS_SELECTOR, 'tr.cart_item td.product-name')
    coupon_code_field = (By.ID, 'coupon_code')
    apply_coupon_button = (By.CSS_SELECTOR, 'button[name="apply_coupon"]')
    cart_page_message = (By.CSS_SELECTOR, 'div.woocommerce-message')
    proceed_to_checkout = (By.CSS_SELECTOR, 'div.wc-proceed-to-checkout')

