from BaseTest import BaseTest

# TestHomepage
# Written by Angela Korra'ti
# Last updated 2/7/2019
#
# This class conducts tests against the homepage of my test Wordpress site.

class TestHomepage(BaseTest):
    def setUp(self):
        '''Do setup for the test cases.'''
        super().setUp()
        self.driver.get(self.wpLib.wpBaseUri)

    def testHomepageTitle(self):
        '''Verify that the homepage has the correct title.'''
        title = self.driver.find_element_by_class_name(self.wpLib.siteTitle['class'])
        assert title.text == self.wpLib.siteTitle['text']
        assert title.is_displayed() is True

    def testHomepageDescription(self):
        '''Verify that the homepage has the correct description.'''
        description = self.driver.find_element_by_class_name(self.wpLib.siteDescription['class'])
        assert description.text == self.wpLib.siteDescription['text']
        assert description.is_displayed() is True