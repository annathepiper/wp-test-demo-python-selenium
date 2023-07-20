import WPHomepage
from BaseTest import BaseTest

# TestHomepageMenu
# Written by Angela Korra'ti
# Last updated 7/19/2023
#
# This class conducts tests against the menu on the homepage of my test WordPress site.


class TestHomepageMenu(BaseTest):
    wp_menu = None

    def setup_method(self):
        """
        Do setup for the test cases.
        """
        super().setup_method()
        self.driver.get(self.wp_lib.wp_base_uri)
        self.wp_menu = WPHomepage.WPHomepage(self.driver, self.wp_lib).wp_menu

    def test_home_menu(self):
        """
        Verify the homepage Home menu is present, visible, and has the correct text and destination
        """
        self.wp_menu.verify_home_menu()

    def test_about_menu(self):
        """
        Verify the homepage About menu is present, visible, and has the correct text and destination
        """
        self.wp_menu.verify_about_menu()

    def test_books_menu(self):
        """
        Verify the homepage Books menu is present, visible, and has the correct text and destination
        """
        self.wp_menu.verify_books_menu()

    def test_blog_menu(self):
        """
        Verify the homepage Blog menu is present, visible, and has the correct text and destination
        """
        self.wp_menu.verify_blog_menu()

    def test_contact_menu(self):
        """
        Verify the homepage Contact menu is present, visible, and has the correct text and destination
        """
        self.wp_menu.verify_contact_menu()

    def test_store_menu(self):
        """
        Verify the homepage Store menu is present, visible, and has the correct text and destination
        """
        self.wp_menu.verify_store_menu()
