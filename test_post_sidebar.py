import WPPost
import pytest

# TestPostSidebar
# Written by Angela Korra'ti
# Last updated 7/21/2023
#
# This class conducts tests against the menu on a post of my test WordPress site.


@pytest.mark.usefixtures("setup_webdriver", "wp_lib")
class TestPostSidebar:
    wp_sidebar = None

    def setup_method(self):
        """
        Do setup for the test cases.
        """
        self.driver.get(self.wp_lib.wp_post_uri)
        self.wp_sidebar = WPPost.WPPost(self.driver, self.wp_lib).wp_sidebar

    def test_search_widget(self):
        """
        Verify a post sidebar search widget is present and visible
        """
        self.wp_sidebar.verify_search_widget()

    def test_search_input(self):
        """
        Verify a post sidebar search input box is present and visible and has the expected text
        """
        self.wp_sidebar.verify_search_input()

    def test_search_button(self):
        """
        Verify a post sidebar search button exists and is visible
        """
        self.wp_sidebar.verify_search_button()

    def test_recent_posts(self):
        """
        Verify a post recent posts widget is present and visible, has the correct title, and has five posts
        """
        self.wp_sidebar.verify_recent_posts()

    def test_recent_comments(self):
        """
        Verify a post recent comments widget is present and visible, and has the correct title and comment count
        """
        self.wp_sidebar.verify_recent_comments()

    def test_archives(self):
        """
        Verify a post archives widget is present and visible, and has the correct title and link count
        """
        self.wp_sidebar.verify_archives()

    def test_categories(self):
        """
        Verify a post categories widget is present and visible, and has the correct title and link count
        """
        self.wp_sidebar.verify_categories()

    def test_meta(self):
        """
        Verify a post meta widget is present and visible, and has the correct title and link count
        """
        self.wp_sidebar.verify_meta()
