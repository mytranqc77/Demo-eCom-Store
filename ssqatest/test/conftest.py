import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOption
from selenium.webdriver.firefox.options import Options as FirefoxOption

import os


@pytest.fixture(scope="class")
def init_driver(request):
    # os.environ['BROWSER'] = 'chrome'
    supported_browsers = ['chrome', 'ch', 'headlesschrome', 'firefox', 'ff', 'headlessfirefox']

    browser = os.environ.get('BROWSER', 'chrome')
    if not browser:
        raise Exception("The environment variable 'BROWSER' must be set")

    browser = browser.lower()
    if browser not in supported_browsers:
        raise Exception(f"Provided browser '{browser}'is not one of the supported browser")

    if browser in ('chrome', 'ch'):
        driver = webdriver.Chrome()
    elif browser in ('firefox', 'ff'):
        driver = webdriver.Firefox()
    elif browser in 'headlesschrome':
        chrome_options = ChromeOption()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
    elif browser in 'headlessfirefox':
        firefox_options = FirefoxOption()
        firefox_options.add_argument('--disable-gpu')
        firefox_options.add_argument('--no-sandbox')
        firefox_options.add_argument('--headless')
        driver = webdriver.Firefox(options=firefox_options)

    request.cls.driver = driver # makes the driver available as self.driver inside the test class.

    yield
    # driver.quit()
