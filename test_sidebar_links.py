from BaseTest import BaseTest
import WPPost
from selenium.webdriver.common.by import By

# TestSidebarLinks
# Written by Angela Korra'ti
# Last updated 7/7/2023
#
# This class conducts tests against the sidebar of my test WordPress site.


class TestSidebarLinks(BaseTest):
    wp_sidebar = None

    def set_wp_sidebar(self, wp_sidebar):
        """
        Setup function to set the class variable wp_sidebar used in child tests.
        """
        self.wp_sidebar = wp_sidebar

    def verify_recent_posts_link_click(self):
        """
        Verify clicking the first link in the Recent Posts links goes to the expected post
        """
        self.ac.move_to_element(self.wp_sidebar.search_element).perform()
        self.wp_sidebar.recent_posts_list_elements[0].click()
        assert self.driver.current_url == self.wp_lib.wp_base_uri + self.wp_lib.recent_posts_uri
        wp_post = WPPost.WPPost(self.driver, self.wp_lib)
        assert wp_post.post_title_element is not None
        assert wp_post.post_title_element.is_displayed()
        assert wp_post.post_title_text == self.wp_lib.recent_posts_title

    def verify_recent_comments_link_click(self):
        """
        Verify clicking the first link in the Recent Comments links goes to the expected comment
        """
        self.ac.move_to_element(self.wp_sidebar.recent_posts_list_elements[4]).perform()
        self.wp_sidebar.recent_comments_list_elements[0].click()

        # 7/7/2023 Looking for MOST of the URI here because the actual comment number changes
        # depending on when I last set up the test Wordpress database, or if I had to import
        # multiple times
        most_of_uri = self.wp_lib.wp_base_uri + self.wp_lib.recent_comments_uri
        assert self.driver.current_url.startswith(most_of_uri)
        wp_post = WPPost.WPPost(self.driver, self.wp_lib)
        assert wp_post.post_title_element is not None
        assert wp_post.post_title_element.is_displayed()
        assert wp_post.post_title_text == self.wp_lib.recent_comments_title

    def verify_archives_link_click(self):
        """
        Verify clicking the first link in the Archives links goes to the expected archives page
        """
        self.ac.move_to_element(self.wp_sidebar.archives_element).perform()
        self.wp_sidebar.archives_list_elements[0].click()
        assert self.driver.current_url == self.wp_lib.wp_base_uri + self.wp_lib.archives_uri
        page_title = self.driver.find_element(By.CLASS_NAME, self.wp_lib.page_title_class)
        assert page_title is not None
        assert page_title.is_displayed()
        assert page_title.text == self.wp_lib.archives_string + self.wp_lib.archives_title

    def verify_categories_link_click(self):
        """
        Verify clicking the first link in the Categories links goes to the expected category page
        """
        self.ac.move_to_element(self.wp_sidebar.categories_element).perform()
        self.wp_sidebar.categories_list_elements[0].click()
        assert self.driver.current_url == self.wp_lib.wp_base_uri + self.wp_lib.categories_uri
        page_title = self.driver.find_element(By.CLASS_NAME, self.wp_lib.page_title_class)
        assert page_title is not None
        assert page_title.is_displayed()
        assert page_title.text == self.wp_lib.categories_string + self.wp_lib.categories_title
