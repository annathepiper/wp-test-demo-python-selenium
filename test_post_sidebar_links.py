from test_sidebar_links import TestSidebarLinks
import WPPost

# TestPostSidebarLinks
# Written by Angela Korra'ti
# Last updated 7/6/2023
#
# This class conducts tests against the sidebar of my test WordPress site.


class TestPostSidebarLinks(TestSidebarLinks):
    wp_sidebar = None

    def setup_method(self):
        """
        Do setup for the test cases.
        """
        super().setup_method()
        self.driver.get(self.wp_lib.wp_post_uri)
        super().set_wp_sidebar(WPPost.WPPost(self.driver, self.wp_lib).wp_sidebar)

    def test_recent_posts_link_click(self):
        """
        Verify clicking the first link in the Recent Posts links goes to the expected post from a post
        """
        self.verify_recent_posts_link_click()

    def test_recent_comments_link_click(self):
        """
        Verify clicking the first link in the Recent Comments links goes to the expected comment from a post
        """
        self.verify_recent_comments_link_click()

    def test_archives_link_click(self):
        """
        Verify clicking the first link in the Archives links goes to the expected archives page from a post
        """
        self.verify_archives_link_click()

    def test_categories_link_click(self):
        """
        Verify clicking the first link in the Categories links goes to the expected category page from a post
        """
        self.verify_categories_link_click()
