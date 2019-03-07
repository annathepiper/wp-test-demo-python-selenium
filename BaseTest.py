import os
from selenium import webdriver
import unittest
import WPTestLib

# BaseTest
# Written by Angela Korra'ti
# Last updated 2/11/2019
#
# This is the base test class for the other ones in the suite.


class BaseTest(unittest.TestCase):
    driver = None
    wp_lib = None

    def setUp(self):
        """
        Global setup function for all test classes that are children of BaseTest
        """
        self.wp_lib = WPTestLib.WPTestLib()
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        self.driver = webdriver.Remote(
            command_executor=self.wp_lib.selenium_host,
            desired_capabilities=caps)

    def tearDown(self):
        """
        Global teardown function for all test classes that are children of BaseTest
        :return:
        """
        self.driver.close()
        self.driver.quit()
