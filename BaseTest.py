import os
from selenium import webdriver
import unittest
import WPTestLib

# BaseTest
# Written by Angela Korra'ti
# Last updated 2/7/2019
#
# This is the base test class for the other ones in the suite.

class BaseTest(unittest.TestCase):
    driver = None
    wpLib = None

    def setUp(self):
        self.wpLib = WPTestLib.WPTestLib()
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        self.driver = webdriver.Remote(
            command_executor=self.wpLib.seleniumHost,
            desired_capabilities=caps)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()