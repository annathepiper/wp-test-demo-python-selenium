from TestFooter import TestFooter
import WPHomepage
from selenium.webdriver.common.action_chains import ActionChains

# TestFooter
# Written by Angela Korra'ti
# Last updated 4/23/2019
#
# This class conducts tests against the footer on a post of my test Wordpress site.


class TestPostFooter(TestFooter):
    wp_footer = None
    ac = None

    def setUp(self):
        """
        Do setup for the test cases.
        """
        super().setUp()
        self.driver.get(self.wp_lib.wp_post_uri)
        self.wp_footer = WPHomepage.WPHomepage(self.driver, self.wp_lib).wp_footer
        self.ac = ActionChains(self.driver)

    def TestFooterSiteTitle(self):
        """
        Verify the footer site title element is present and visible on a post
        """
