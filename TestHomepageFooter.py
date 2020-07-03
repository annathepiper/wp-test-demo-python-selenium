from TestFooter import TestFooter
import WPHomepage

# TestFooter
# Written by Angela Korra'ti
# Last updated 4/24/2019
#
# This class conducts tests against the footer on the homepage of my test Wordpress site.


class TestHomepageFooter(TestFooter):
    wp_footer = None

    def setUp(self):
        """
        Do setup for the test cases.
        """
        super().setUp()
        self.driver.get(self.wp_lib.wp_base_uri)
        self.wp_footer = WPHomepage.WPHomepage(self.driver, self.wp_lib).wp_footer

    def test_site_title(self):
        """
        Verify the footer site title element is present and visible on the homepage
        """
        self.verify_site_title(self.wp_footer)

    def test_site_title_text(self):
        """
        Verify that the homepage footer site title element has the correct text
        """
        self.verify_site_title_text(self.wp_footer)

    def test_site_title_link_click(self):
        """
        Verify clicking on the homepage footer site title link takes you to the homepage
        """
        self.verify_site_title_link_click(self.wp_footer)

    def test_wordpress(self):
        """
        Verify the homepage footer Wordpress element is present and visible
        """
        self.verify_wordpress(self.wp_footer)

    def test_wordpress_text(self):
        """
        Verify that the homepage footer Wordpress element has the correct text
        """
        self.verify_wordpress_text(self.wp_footer)

    def test_wordpress_link_click(self):
        """
        Verify that clicking on the homepage footer Wordpress link lands on correct page (wordpress.org)
        """
        self.verify_wordpress_link_click(self.wp_footer)

    def test_social_facebook(self):
        """
        Verify the homepage footer Facebook element is present and visible
        """
        self.verify_social_facebook(self.wp_footer)

    def test_social_facebook_text(self):
        """
        Verify that the homepage footer Facebook element has the correct text
        """
        self.verify_social_facebook_text(self.wp_footer)

    def test_social_facebook_link_click(self):
        """
        Verify that clicking the homepage footer Facebook link lands on correct page
        """
        self.verify_social_facebook_link_click(self.wp_footer)

    def test_social_twitter(self):
        """
        Verify the homepage footer Twitter element is present and visible
        """
        self.verify_social_twitter(self.wp_footer)

    def test_social_twitter_text(self):
        """
        Verify that the homepage footer Twitter element has the correct text
        """
        self.verify_social_twitter_text(self.wp_footer)

    def test_social_twitter_link_click(self):
        """
        Verify that clicking the homepage footer Twitter link lands on correct page
        """
        self.verify_social_twitter_link_click(self.wp_footer)

    def test_social_github(self):
        """
        Verify the homepage footer Github element is present and visible
        """
        self.verify_social_github(self.wp_footer)

    def test_social_github_text(self):
        """
        Verify that the homepage footer Github element has the correct text
        """
        self.verify_social_github_text(self.wp_footer)

    def test_social_github_link_click(self):
        """
        Verify that clicking the homepage footer Github link lands on correct page
        """
        self.verify_social_github_link_click(self.wp_footer)

    def test_social_linkedin(self):
        """
        Verify the homepage footer LinkedIn element is present and visible
        """
        self.verify_social_linkedin(self.wp_footer)

    def test_social_linkedin_text(self):
        """
        Verify that the homepage footer LinkedIn element has the correct text
        """
        self.verify_social_linkedin_text(self.wp_footer)

    def test_social_linkedin_link_click(self):
        """
        Verify that clicking the homepage footer LinkedIn link lands on correct page
        """
        self.verify_social_linkedin_link_click(self.wp_footer)
