import WPHomepage
import pytest

# TestHomepage
# Written by Angela Korra'ti
# Last updated 7/21/2023
#
# This class conducts tests against the homepage of my test WordPress site.


@pytest.mark.usefixtures("setup_webdriver", "wp_lib")
class TestHomepage:
    wp_homepage = None
    wp_menu = None

    def setup_method(self):
        """
        Do setup for the test cases.
        """
        # super().setup_method()
        self.driver.get(self.wp_lib.wp_base_uri)
        # self.wp_homepage = WPHomepage.WPHomepage(self.driver, self.wp_lib)
        self.wp_homepage = WPHomepage.WPHomepage(self.wp_lib)
        self.wp_menu = self.wp_homepage.wp_menu

    def test_homepage_title(self):
        """
        Verify that the homepage has the correct title
        """
        assert self.wp_homepage.site_title == self.wp_lib.site_title['text']
        assert self.wp_homepage.site_title_element.is_displayed() is True

    def test_homepage_description(self):
        """
        Verify that the homepage has the correct description
        """
        assert self.wp_homepage.site_description == self.wp_lib.site_description['text']
        assert self.wp_homepage.site_description_element.is_displayed() is True

    def test_primary_menu_exists_visible(self):
        """
        Verify that the primary menu is present and visible on the homepage
        """
        menu = self.wp_menu.menu_element
        assert menu is not None
        assert menu.is_displayed()

    def test_content_area_exists_visible(self):
        """
        Verify that the overall content area is present and visible on the homepage
        """
        content = self.wp_homepage.content_area_element
        assert content is not None
        assert content.is_displayed()

    def test_primary_content_area_exists_visible(self):
        """
        Verify that the primary content area is present and visible on the homepage
        """
        content = self.wp_homepage.primary_content_area_element
        assert content is not None
        assert content.is_displayed()

    def test_secondary_content_area_exists_visible(self):
        """
        Verify that the secondary content area is present and visible on the homepage
        """
        content = self.wp_homepage.secondary_content_area_element
        assert content is not None
        assert content.is_displayed()

    def test_footer_exists_visible(self):
        """
        Verify that the footer is present and visible on the homepage
        """
        footer = self.wp_homepage.wp_footer.footer_element
        assert footer is not None
        assert footer.is_displayed()

    def test_footer_social_menu_exists_visible(self):
        """
        Verify that the footer social menu is present and visible on the homepage
        """
        social_menu = self.wp_homepage.wp_footer.social_menu_element
        assert social_menu is not None
        assert social_menu.is_displayed()

    def test_footer_site_info_exists_visible(self):
        """
        Verify that the footer site info section is present and visible on the homepage
        """
        site_info = self.wp_homepage.wp_footer.site_info_element
        assert site_info is not None
        assert site_info.is_displayed()
