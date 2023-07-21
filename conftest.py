import pytest
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver
import WPTestLib


@pytest.fixture(scope="class", autouse=True)
def setup_webdriver(request):
    selenium_host = "http://localhost:4444/wd/hub"
    options = ChromeOptions()
    options.set_capability('browserName', os.getenv('BROWSER', 'chrome'))
    driver = webdriver.Remote(selenium_host, options=options)
    request.cls.driver = driver
    yield driver
    driver.close()
    driver.quit()

@pytest.fixture(scope="class", autouse=True)
def action_chains(request, setup_webdriver):
    request.cls.ac = ActionChains(setup_webdriver)

@pytest.fixture(scope="class", autouse=True)
def wp_lib(request):
    request.cls.wp_lib = WPTestLib.WPTestLib()