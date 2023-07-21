import WPPost
import pytest

# TestPost
# Written by Angela Korra'ti
# Last updated 7/6/2023
#
# This class conducts tests against a post on my test WordPress site.


@pytest.mark.usefixtures("setup_webdriver", "wp_lib")
class TestPost:
    wp_post = None
    wp_menu = None

    def setup_method(self):
        """
        Do setup for the test cases.
        """
        self.driver.get(self.wp_lib.wp_post_uri)
        self.wp_post = WPPost.WPPost(self.driver, self.wp_lib)
        self.wp_menu = self.wp_post.wp_menu

    def test_post_site_title(self):
        """
        Verify that the post has the correct site title
        """
        assert self.wp_post.site_title == self.wp_lib.site_title['text']
        assert self.wp_post.site_title_element.is_displayed() is True

    def test_post_site_description(self):
        """
        Verify that the post has the correct site description
        """
        assert self.wp_post.site_description == self.wp_lib.site_description['text']
        assert self.wp_post.site_description_element.is_displayed() is True

    def test_post_title(self):
        """
        Verify that the post shows its correct title
        """
        assert self.wp_post.post_title_text == self.wp_lib.post_title
        assert self.wp_post.post_title_element.is_displayed() is True

    def test_primary_menu_exists_visible(self):
        """
        Verify that the primary menu is present and visible on the post
        """
        menu = self.wp_menu.menu_element
        assert menu is not None
        assert menu.is_displayed()

    def test_content_area(self):
        """
        Verify that the overall content area is present and visible on the post
        """
        content = self.wp_post.content_area_element
        assert content is not None
        assert content.is_displayed()

    def test_primary_content_area_exists_visible(self):
        """
        Verify that the primary content area is present and visible on the post
        """
        content = self.wp_post.primary_content_area_element
        assert content is not None
        assert content.is_displayed()

    def test_secondary_content_area_exists_visible(self):
        """
        Verify that the secondary content area is present and visible on the post
        """
        content = self.wp_post.secondary_content_area_element
        assert content is not None
        assert content.is_displayed()

    def test_footer_exists_visible(self):
        """
        Verify that the footer is present and visible on the post
        """
        footer = self.wp_post.wp_footer.footer_element
        assert footer is not None
        assert footer.is_displayed()

    def test_footer_social_menu_exists_visible(self):
        """
        Verify that the footer social menu is present and visible on the post
        """
        social_menu = self.wp_post.wp_footer.social_menu_element
        assert social_menu is not None
        assert social_menu.is_displayed()

    def test_footer_site_info_exists_visible(self):
        """
        Verify that the footer site info section is present and visible on the post
        """
        site_info = self.wp_post.wp_footer.site_info_element
        assert site_info is not None
        assert site_info.is_displayed()
