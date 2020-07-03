import os
from selenium import webdriver
import WPTestLib
from selenium.webdriver.common.action_chains import ActionChains
from abc import ABC

# BaseTest
# Written by Angela Korra'ti
# Last updated 4/26/2019
#
# This is the base test class for the other ones in the suite.


class BaseTest(ABC):
    driver = None
    wp_lib = None
    ac = None

    def setUp(self):
        """
        Global setup function for all test classes that are children of BaseTest
        """
        self.wp_lib = WPTestLib.WPTestLib()
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        self.driver = webdriver.Remote(
            command_executor=self.wp_lib.selenium_host,
            desired_capabilities=caps)
        self.ac = ActionChains(self.driver)

    def tearDown(self):
        """
        Global teardown function for all test classes that are children of BaseTest
        :return:
        """
        self.driver.close()
        self.driver.quit()
