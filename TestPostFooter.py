from TestFooter import TestFooter
import WPPost

# TestFooter
# Written by Angela Korra'ti
# Last updated 4/26/2019
#
# This class conducts tests against the footer on a post of my test Wordpress site.


class TestPostFooter(TestFooter):
    def setUp(self):
        """
        Do setup for the test cases.
        """
        super().setUp()
        self.driver.get(self.wp_lib.wp_post_uri)
        super().set_wp_footer(WPPost.WPPost(self.driver, self.wp_lib).wp_footer)

    def test_site_title(self):
        """
        Verify the footer site title on a post
        """
        self.verify_site_title()

    def test_wordpress(self):
        """
        Verify the footer Wordpress element on a post
        """
        self.verify_wordpress()

    def test_social_facebook(self):
        """
        Verify the footer Facebook element on a post
        """
        self.verify_social_facebook()

    def test_social_twitter(self):
        """
        Verify the footer Twitter element on a post
        """
        self.verify_social_twitter()

    def test_social_github(self):
        """
        Verify the footer Github element on a post
        """
        self.verify_social_github()

    def test_social_linkedin(self):
        """
        Verify the footer LinkedIn element on a post
        """
        self.verify_social_linkedin()
