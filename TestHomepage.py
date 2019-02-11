from BaseTest import BaseTest
import WPHomepage

# TestHomepage
# Written by Angela Korra'ti
# Last updated 2/11/2019
#
# This class conducts tests against the homepage of my test Wordpress site.


class TestHomepage(BaseTest):
    wp_homepage = None

    def setUp(self):
        """
        Do setup for the test cases.
        """
        super().setUp()
        self.driver.get(self.wp_lib.wp_base_uri)
        self.wp_homepage = WPHomepage.WPHomepage(self.driver, self.wp_lib)

    def testHomepageTitle(self):
        """
        Verify that the homepage has the correct title
        """
        assert self.wp_homepage.site_title == self.wp_lib.site_title['text']
        assert self.wp_homepage.site_title_element.is_displayed() is True

    def testHomepageDescription(self):
        """
        Verify that the homepage has the correct description
        """
        assert self.wp_homepage.site_description == self.wp_lib.site_description['text']
        assert self.wp_homepage.site_description_element.is_displayed() is True

    def testPrimaryMenuExistsVisible(self):
        """
        Verify that the primary menu is present and visible on the homepage
        """
        menu = self.wp_homepage.primary_menu_element
        assert menu is not None
        assert menu.is_displayed()

    def testContentAreaExistsVisible(self):
        """
        Verify that the overall content area is present and visible on the homepage
        """
        content = self.wp_homepage.content_area_element
        assert content is not None
        assert content.is_displayed()

    def testPrimaryContentAreaExistsVisible(self):
        """
        Verify that the primary content area is present and visible on the homepage
        """
        content = self.wp_homepage.primary_content_area_element
        assert content is not None
        assert content.is_displayed()

    def testSecondaryContentAreaExistsVisible(self):
        """
        Verify that the secondary content area is present and visible on the homepage
        """
        content = self.wp_homepage.secondary_content_area_element
        assert content is not None
        assert content.is_displayed()

    def testFooterExistsVisible(self):
        """
        Verify that the footer is present and visible on the homepage
        """
        footer = self.wp_homepage.footer_element
        assert footer is not None
        assert footer.is_displayed()

    def testFooterSocialMenuExistsVisible(self):
        """
        Verify that the footer social menu is present and visible on the homepage
        """
        footer_social_menu = self.wp_homepage.footer_social_menu_element
        assert footer_social_menu is not None
        assert footer_social_menu.is_displayed()

    def testFooterSiteInfoExistsVisible(self):
        """
        Verify that the footer site info section is present and visible on the homepage
        """
        footer_site_info = self.wp_homepage.footer_site_info_element
        assert footer_site_info is not None
        assert footer_site_info.is_displayed()
