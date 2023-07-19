from test_login_logout import TestLoginLogout
import WPPost

# TestPostLoginLogout
# Written by Angela Korra'ti
# Last updated 7/18/2023
#
# This class conducts login and logout testing against a post.


class TestPostLoginLogout(TestLoginLogout):
    wp_sidebar = None

    def setup_method(self):
        """
        Do setup for the test cases.
        """
        super().setup_method()
        self.driver.get(self.wp_lib.wp_post_uri)
        super().set_wp_sidebar(WPPost.WPPost(self.driver, self.wp_lib).wp_sidebar)

    def test_meta_login_link_click(self):
        """
        Verify clicking on the first link in the Meta links goes to the login page from the homepage
        """
        self.verify_meta_login_link_click()
