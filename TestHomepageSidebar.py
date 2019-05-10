from TestSidebar import TestSidebar
import WPHomepage

# TestHomepageSidebar
# Written by Angela Korra'ti
# Last updated 5/10/2019
#
# This class conducts tests against the menu on the homepage of my test WordPress site.


class TestHomepageSidebar(TestSidebar):

    def setUp(self):
        """
        Do setup for the test cases.
        """
        super().setUp()
        self.driver.get(self.wp_lib.wp_base_uri)
        super().set_wp_sidebar(WPHomepage.WPHomepage(self.driver, self.wp_lib).wp_sidebar)

    def test_search_widget(self):
        """
        Verify the homepage sidebar search widget is present and visible
        """
        self.verify_search_widget()

    def test_search_input(self):
        """
        Verify the homepage sidebar search input box is present and visible and has the expected text
        """
        self.verify_search_input()

    def test_search_button(self):
        """
        Verify the homepage sidebar search button exists and is visible
        """
        self.verify_search_button()

    def test_recent_posts(self):
        """
        Verify the homepage recent posts widget is present and visible, has the correct title, and has five posts
        """
        self.verify_recent_posts()

    def test_recent_comments(self):
        """
        Verify the homepage recent comments widget is present and visible, and has the correct title and comment count
        """
        self.verify_recent_comments()

    def test_archives(self):
        """
        Verify the homepage archives widget is present and visible, and has the correct title and link count
        """
        self.verify_archives()

    def test_categories(self):
        """
        Verify the homepage categories widget is present and visible, and has the correct title and link count
        """
        self.verify_categories()

    def test_meta(self):
        """
        Verify the homepage meta widget is present and visible, and has the correct title and link count
        """
        self.verify_meta()
