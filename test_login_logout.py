from test_sidebar_links import TestSidebarLinks

# TestLoginLogout
# Written by Angela Korra'ti
# Last updated 7/18/2023
#
# Parent class for testing the login page. This class conducts tests against the homepage by default.
# Child classes will do appropriate setup to test other pages.


class TestLoginLogout(TestSidebarLinks):
    wp_login = None

    def set_wp_login(self, wp_login):
        """
        Setup function to set the class variable wp_login used in child tests.
        """
        self.wp_login = wp_login

    def verify_meta_login_link_click(self):
        """
        Verify clicking on the first link in the Meta links goes to the login page
        """
        self.ac.move_to_element(self.wp_sidebar.meta_element).perform()
        self.wp_sidebar.meta_list_elements[0].click()
        assert self.driver.current_url == self.wp_lib.wp_base_uri + self.wp_lib.meta_login_uri
        self.driver.back()
