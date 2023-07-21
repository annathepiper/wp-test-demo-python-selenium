import WPPost
import pytest

# TestPostMenu
# Written by Angela Korra'ti
# Last updated 7/21/2023
#
# This class conducts tests against the menu on a post of my test WordPress site.


@pytest.mark.usefixtures("setup_webdriver", "wp_lib")
class TestPostMenu:
    wp_menu = None

    def setup_method(self):
        """
        Do setup for the test cases.
        """
        self.driver.get(self.wp_lib.wp_post_uri)
        self.wp_menu = WPPost.WPPost(self.driver, self.wp_lib).wp_menu

    def test_home_menu(self):
        """
        Verify the post Home menu is present, visible, and has the correct text and destination
        """
        self.wp_menu.verify_home_menu()

    def test_about_menu(self):
        """
        Verify the post About menu is present, visible, and has the correct text and destination
        """
        self.wp_menu.verify_about_menu()

    def test_books_menu(self):
        """
        Verify the post Books menu is present, visible, and has the correct text and destination
        """
        self.wp_menu.verify_books_menu()

    def test_blog_menu(self):
        """
        Verify the post Blog menu is present, visible, and has the correct text and destination
        """
        self.wp_menu.verify_blog_menu()

    def test_contact_menu(self):
        """
        Verify the post Contact menu is present, visible, and has the correct text and destination
        """
        self.wp_menu.verify_contact_menu()

    def test_store_menu(self):
        """
        Verify the post Store menu is present, visible, and has the correct text and destination
        """
        self.wp_menu.verify_store_menu()
