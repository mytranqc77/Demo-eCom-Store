from selenium.webdriver.common.by import By


class CheckoutPageLocators():

    first_name_element = (By.ID, 'billing_first_name')
    last_name_element = (By.ID, 'billing_last_name')
    address_element = (By.ID, 'billing_address_1')
    city_element = (By.ID, 'billing_city')
    zipcode_element = (By.ID, 'billing_postcode')
    phone_element = (By.ID, 'billing_phone')
    email_element = (By.ID, 'billing_email')
    checkout_element = (By.ID, 'place_order')


