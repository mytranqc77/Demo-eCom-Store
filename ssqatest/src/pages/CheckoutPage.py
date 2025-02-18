import time

from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.pages.locators.CheckoutPageLocators import CheckoutPageLocators
from ssqatest.src.helpers.generic_helpers import generate_random_email_and_password


class CheckoutPage(CheckoutPageLocators):
    def __init__(self, driver):
        self.driver = driver
        self.selenium = SeleniumExtended(self.driver)

    def input_billing_first_name(self, firstname=None):
        firstname = firstname if firstname else "TestFirstName"
        self.selenium.wait_and_input_text(self.first_name_element, firstname)
        return firstname

    def input_billing_last_name(self, lastname=None):
        lastname = lastname if lastname else "TestLastName"
        self.selenium.wait_and_input_text(self.last_name_element, lastname)
        return lastname

    def input_billing_address1(self, address1=None):
        address1 = address1 if address1 else "123 Main Str."
        self.selenium.wait_and_input_text(self.address_element, address1)
        return address1

    def input_city(self, city=None):
        city = city if city else "NewYork"
        self.selenium.wait_and_input_text(self.city_element, city)
        return city

    def input_zipcode(self, zipcode=None):
        zipcode = zipcode if zipcode else "94016"
        self.selenium.wait_and_input_text(self.zipcode_element, zipcode)
        return zipcode

    def input_phone(self, phonenumber=None):
        phonenumber = phonenumber if phonenumber else "8403293787"
        self.selenium.wait_and_input_text(self.phone_element, phonenumber)
        return phonenumber

    def input_email(self, email=None):
        random_email = generate_random_email_and_password()
        generated_email = random_email["Email"]
        email = email if email else generated_email
        self.selenium.wait_and_input_text(self.email_element, email)
        return email

    def fill_in_billing_info(self):
        # print(f"Billing info - Firstname: {firstname}, Lastname: {lastname}, "
        #       f"Addess:{address}, City: {city}, Zipcode: {zipcode}, Phonenumber: {phonenumber}, Email :{email}")
        # self.input_billing_first_name()
        # self.input_billing_last_name()
        # self.input_billing_address1()
        # self.input_city()
        # self.input_zipcode()
        # self.input_phone()
        # self.input_email()
        billing_info = {
            "firstname": self.input_billing_first_name(),
            "lastname": self.input_billing_last_name(),
            "address": self.input_billing_address1(),
            "city": self.input_city(),
            "zipcode": self.input_zipcode(),
            "phonenumber": self.input_phone(),
            "email": self.input_email(),

        }
        print(f"Billing info used: {billing_info}")
        return billing_info

    def check_out(self):
        self.selenium.wait_and_click(self.checkout_element)







