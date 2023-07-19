from test_login_logout import TestLoginLogout
import WPHomepage

# TestHomepageLoginLogout
# Written by Angela Korra'ti
# Last updated 7/18/2023
#
# This class conducts tests against the sidebar of my test WordPress site.


class TestHomepageLoginLogout(TestLoginLogout):
    wp_sidebar = None

    def setup_method(self):
        """
        Do setup for the test cases.
        """
        super().setup_method()
        self.driver.get(self.wp_lib.wp_base_uri)
        super().set_wp_sidebar(WPHomepage.WPHomepage(self.driver, self.wp_lib).wp_sidebar)

    def test_meta_login_link_click(self):
        """
        Verify clicking on the first link in the Meta links goes to the login page from the homepage
        """
        self.verify_meta_login_link_click()
