from TestMenu import TestMenu
import WPPost

# TestPostMenu
# Written by Angela Korra'ti
# Last updated 5/10/2019
#
# This class conducts tests against the menu on a post of my test WordPress site.


class TestPostMenu(TestMenu):

    def setUp(self):
        """
        Do setup for the test cases.
        """
        super().setUp()
        self.driver.get(self.wp_lib.wp_post_uri)
        super().set_wp_menu(WPPost.WPPost(self.driver, self.wp_lib).wp_menu)

    def test_home_menu(self):
        """
        Verify the post Home menu is present, visible, and has the correct text and destination
        """
        self.verify_home_menu()

    def test_about_menu(self):
        """
        Verify the post About menu is present, visible, and has the correct text and destination
        """
        self.verify_about_menu()

    def test_books_menu(self):
        """
        Verify the post Books menu is present, visible, and has the correct text and destination
        """
        self.verify_books_menu()

    def test_blog_menu(self):
        """
        Verify the post Blog menu is present, visible, and has the correct text and destination
        """
        self.verify_blog_menu()

    def test_contact_menu(self):
        """
        Verify the post Contact menu is present, visible, and has the correct text and destination
        """
        self.verify_contact_menu()

    def test_store_menu(self):
        """
        Verify the post Store menu is present, visible, and has the correct text and destination
        """
        self.verify_store_menu()
