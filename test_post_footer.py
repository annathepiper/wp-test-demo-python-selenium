import WPPost
import pytest

# TestFooter
# Written by Angela Korra'ti
# Last updated 7/21/2023
#
# This class conducts tests against the footer on a post of my test WordPress site.


@pytest.mark.usefixtures("setup_webdriver", "wp_lib")
class TestPostFooter:
    wp_footer = None

    def setup_method(self):
        """
        Do setup for the test cases.
        """
        self.driver.get(self.wp_lib.wp_post_uri)
        self.wp_footer = WPPost.WPPost(self.driver, self.wp_lib).wp_footer

    def test_site_title(self):
        """
        Verify the footer site title on a post
        """
        self.wp_footer.verify_site_title()

    def test_wordpress(self):
        """
        Verify the footer WordPress element on a post
        """
        self.wp_footer.verify_wordpress()

    def test_social_facebook(self):
        """
        Verify the footer Facebook element on a post
        """
        self.wp_footer.verify_social_facebook()

    def test_social_mastodon(self):
        """
        Verify the footer Mastodon element on a post
        """
        self.wp_footer.verify_social_mastodon()

    def test_social_github(self):
        """
        Verify the footer GitHub element on a post
        """
        self.wp_footer.verify_social_github()

    def test_social_linkedin(self):
        """
        Verify the footer LinkedIn element on a post
        """
        self.wp_footer.verify_social_linkedin()
