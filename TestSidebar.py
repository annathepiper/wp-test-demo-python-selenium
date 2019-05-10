from BaseTest import BaseTest

# TestSidebar
# Written by Angela Korra'ti
# Last updated 5/10/2019
#
# This class conducts tests against the sidebar of my test WordPress site.


class TestSidebar(BaseTest):
    wp_sidebar = None

    def set_wp_sidebar(self, wp_sidebar):
        """
        Setup function to set the class variable wp_sidebar used in child tests.
        """
        self.wp_sidebar = wp_sidebar

    def verify_search_widget(self):
        """
        Verify that the sidebar search widget is present and visible
        """
        search_widget = self.wp_sidebar.search_element
        assert search_widget is not None
        assert search_widget.is_displayed()

    def verify_search_input(self):
        """
        Verify that the sidebar search input box is present and visible and has the expected text
        """
        search_input = self.wp_sidebar.search_input_element
        assert search_input is not None
        assert search_input.is_displayed()
        search_input_text = self.wp_sidebar.search_input_element.get_attribute("placeholder")
        assert search_input_text == self.wp_lib.sidebar_search_input_text

    def verify_search_button(self):
        """
        Verify that the sidebar search button exists and is visible
        """
        search_button = self.wp_sidebar.search_button_element
        assert search_button is not None
        assert search_button.is_displayed()

    def verify_recent_posts(self):
        """
        Verify that the recent posts widget is present and visible, has the correct title, and has five posts
        """
        recent_posts_widget = self.wp_sidebar.recent_posts_element
        assert recent_posts_widget is not None
        assert recent_posts_widget.is_displayed()
        recent_posts_title = self.wp_sidebar.recent_posts_title_element
        assert recent_posts_title is not None
        assert recent_posts_title.is_displayed()
        assert self.wp_sidebar.recent_posts_title_text == self.wp_lib.sidebar_recent_posts_title_text
        recent_posts_list = self.wp_sidebar.recent_posts_list_element
        assert recent_posts_list is not None
        assert recent_posts_list.is_displayed()
        recent_posts_list_items = self.wp_sidebar.recent_posts_list_items_elements
        assert len(recent_posts_list_items) == 5

    def verify_recent_comments(self):
        """
        Verify the recent comments widget is present and visible, and has the correct title and comment count
        """
        recent_comments_widget = self.wp_sidebar.recent_comments_element
        assert recent_comments_widget is not None
        assert recent_comments_widget.is_displayed()
        recent_comments_title = self.wp_sidebar.recent_comments_title_element
        assert recent_comments_title is not None
        assert recent_comments_title.is_displayed()
        assert self.wp_sidebar.recent_comments_title_text == self.wp_lib.sidebar_recent_comments_title_text
        recent_comments_list = self.wp_sidebar.recent_comments_list_element
        assert recent_comments_list is not None
        assert recent_comments_list.is_displayed()
        recent_comments_list_items = self.wp_sidebar.recent_comments_list_items_elements
        assert len(recent_comments_list_items) >= 1

    def verify_archives(self):
        """
        Verify the archives widget is present and visible, has the correct title, and has the correct count of links
        """
        archives_widget = self.wp_sidebar.archives_element
        assert archives_widget is not None
        assert archives_widget.is_displayed()
        archives_title = self.wp_sidebar.archives_title_element
        assert archives_title is not None
        assert archives_title.is_displayed()
        assert self.wp_sidebar.archives_title_text == self.wp_lib.sidebar_archives_title_text
        archives_list = self.wp_sidebar.archives_list_element
        assert archives_list is not None
        assert archives_list.is_displayed()
        archives_list_items = self.wp_sidebar.archives_list_items_elements
        assert len(archives_list_items) >= 1

    def verify_categories(self):
        """
        Verify the categories widget is present and visible, has the correct title, and has the correct count of links
        """
        categories_widget = self.wp_sidebar.categories_element
        assert categories_widget is not None
        assert categories_widget.is_displayed()
        categories_title = self.wp_sidebar.categories_title_element
        assert categories_title is not None
        assert categories_title.is_displayed()
        assert self.wp_sidebar.categories_title_text == self.wp_lib.sidebar_categories_title_text
        categories_list = self.wp_sidebar.categories_list_element
        assert categories_list is not None
        assert categories_list.is_displayed()
        categories_list_items = self.wp_sidebar.categories_list_items_elements
        assert len(categories_list_items) >= 1

    def verify_meta(self):
        """
        Verify that the meta widget is present and visible, has the correct title, and has the correct count of links
        """
        meta_widget = self.wp_sidebar.meta_element
        assert meta_widget is not None
        assert meta_widget.is_displayed()
        meta_title = self.wp_sidebar.meta_title_element
        assert meta_title is not None
        assert meta_title.is_displayed()
        assert self.wp_sidebar.meta_title_text == self.wp_lib.sidebar_meta_title_text
        meta_list = self.wp_sidebar.meta_list_element
        assert meta_list is not None
        assert meta_list.is_displayed()
        meta_list_items = self.wp_sidebar.meta_list_items_elements
        assert len(meta_list_items) == 4
