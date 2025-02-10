import logging
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from ssqatest.src.pages.locators.MyAccountSignedOutLocator import MyAccountSignedOutLocator
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__) # Get the logger after configuration


class SeleniumExtended:
    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 10

    def wait_and_input_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, self.default_timeout).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    # def wait_and_click(self, locator, timeout=None):
    #     timeout = timeout if timeout else self.default_timeout
    #     try:
    #         WebDriverWait(self.driver, self.default_timeout).until(
    #             EC.visibility_of_element_located(locator)
    #         ).click()
    #     except StaleElementReferenceException:
    #         time.sleep(2)
    #         WebDriverWait(self.driver, self.default_timeout).until(
    #             EC.visibility_of_element_located(locator)
    #         ).click()

    def wait_and_click(self, locator, timeout=None, retries=3):
        timeout = timeout if timeout else self.default_timeout
        for attempt in range(retries):
            try:
                WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable(locator)
                ).click()
                return True
            except StaleElementReferenceException:
                logger.warning(f'StaleElementReferenceException, retrying ({attempt + 1} / {retries})')
                time.sleep(1)
                # print(f'StaleElementReferenceException, retrying ({attempt + 1} / {retries})')
                continue
            except TimeoutException:
                logger.error(f"Timeout: unable to click element {locator} within timeout seconds")
                if attempt == retries - 1:
                    raise
            except Exception as e:
                logger.error(f"An unexpected error occured: {e}")
                raise
        raise TimeoutException(f"Element not clickable after {retries} retries")

    def wait_until_element_contains_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )

    def wait_until_element_is_visible(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    # def wait_and_get_elements(self, locator, timeout=None, error=None):
    #     timeout = timeout if timeout else self.default_timeout
    #     timeout_error_message = error if error else \
    #         f"Unable to find elements located by {locator}"\
    #         f"after timeout of {timeout}"
    #     try:
    #         elements = WebDriverWait(self.driver, timeout).until(
    #             EC.visibility_of_all_elements_located(locator)
    #         )
    #     except TimeoutException:
    #         raise TimeoutException(timeout_error_message)
    #
    #     return elements

    def wait_and_get_elements(self, locator, timeout=None, error=None):
        if not isinstance(locator, tuple) or len(locator) != 2:
            raise ValueError("Locator must be a tuple of the form (By, value).")
        timeout = timeout if timeout else self.default_timeout
        timeout_error_message = error if error else \
            f"Unable to find elements located by {locator} after timeout of {timeout}"
        try:
            logger.info(f"Waiting for elements located by {locator} for up to {timeout}seconds.")
            elements = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
            logger.info(f"Found {len(elements)} elements located by {locator}")
        except TimeoutException:
            logger.info(timeout_error_message)
            raise TimeoutException(timeout_error_message)
        return elements
        # if not isinstance(locator, tuple) or len(locator) != 2:
        #     raise ValueError("Locator must be a tuple of the form (By, value).")
        #
        # timeout = timeout if timeout else self.default_timeout
        # timeout_error_message = error if error else \
        #     f"Unable to find elements located by {locator} after timeout of {timeout}"
        #
        # try:
        #     logger.info(f"Waiting for elements located by {locator} for up to {timeout} seconds.")
        #     elements = WebDriverWait(self.driver, timeout).until(
        #         EC.visibility_of_all_elements_located(locator)
        #     )
        #     logger.info(f"Found {len(elements)} elements located by {locator}.")
        # except TimeoutException:
        #     logger.error(timeout_error_message)
        #     raise TimeoutException(timeout_error_message)
        #
        # return elements

    def wait_and_get_text(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element_text = element.text
        return element_text




