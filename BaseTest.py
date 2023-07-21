import os
from selenium import webdriver
import WPTestLib
from selenium.webdriver.common.action_chains import ActionChains
from abc import ABC
from selenium.webdriver.chrome.options import Options as ChromeOptions
import pytest

# BaseTest
# Written by Angela Korra'ti
# Last updated 7/5/2023
#
# This is the base test class for the other ones in the suite.


class BaseTest(ABC):
    # driver = None
    # wp_lib = None
    # ac = None

    def setup_method(self):
        """
        Global setup function for all test classes that are children of BaseTest
        """
        # self.wp_lib = WPTestLib.WPTestLib()
        # options = ChromeOptions()
        # options.set_capability('browserName', os.getenv('BROWSER', 'chrome'))
        # self.driver = webdriver.Remote(self.wp_lib.selenium_host, options=options)
        # self.ac = ActionChains(self.driver)

    # def teardown_method(self):
    #     """
    #     Global teardown function for all test classes that are children of BaseTest
    #     :return:
    #     """
    #     self.driver.close()
    #     self.driver.quit()
