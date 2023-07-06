from test_footer import TestFooter
import WPHomepage

# TestHomepageFooter
# Written by Angela Korra'ti
# Last updated 7/6/2023
#
# This class conducts tests against the footer on the homepage of my test Wordpress site.


class TestHomepageFooter(TestFooter):

    def setup_method(self):
        """
        Do setup for the test cases.
        """
        super().setup_method()
        self.driver.get(self.wp_lib.wp_base_uri)
        super().set_wp_footer(WPHomepage.WPHomepage(self.driver, self.wp_lib).wp_footer)

    def test_site_title(self):
        """
        Verify the footer site title on the homepage
        """
        self.verify_site_title()

    def test_wordpress(self):
        """
        Verify the footer Wordpress element on the homepage
        """
        self.verify_wordpress()

    def test_social_facebook(self):
        """
        Verify the footer Facebook element on the homepage
        """
        self.verify_social_facebook()

    def test_social_mastodon(self):
        """
        Verify the footer Mastodon element on the homepage
        """
        self.verify_social_mastodon()

    def test_social_github(self):
        """
        Verify the footer Github element on the homepage
        """
        self.verify_social_github()

    def test_social_linkedin(self):
        """
        Verify the footer LinkedIn element on the homepage
        """
        self.verify_social_linkedin()
