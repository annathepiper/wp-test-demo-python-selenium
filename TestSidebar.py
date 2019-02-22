from BaseTest import BaseTest
import WPHomepage

# TestSidebar
# Written by Angela Korra'ti
# Last updated 2/21/2019
#
# This class conducts tests against the sidebar of my test Wordpress site.


class TestSidebar(BaseTest):
    wp_sidebar = None

    def setUp(self):
        """
        Do setup for the test cases.
        """
        super().setUp()
        self.driver.get(self.wp_lib.wp_base_uri)
        self.wp_sidebar = WPHomepage.WPHomepage(self.driver, self.wp_lib).wp_sidebar

    def TestSearchWidgetExistsVisible(self):
        """
        Verify that the sidebar search widget is present and visible
        """
        search_widget = self.wp_sidebar.sidebar_search_element
        assert search_widget is not None
        assert search_widget.is_displayed()

    def TestSearchInputExistsVisible(self):
        """
        Verify that the sidebar search input box is present and visible
        """
        search_input = self.wp_sidebar.sidebar_search_input_element
        assert search_input is not None
        assert search_input.is_displayed()

    def TestSearchInputText(self):
        """
        Verify that the sidebar search input box has the expected text
        """
        search_input_text = self.wp_sidebar.sidebar_search_input_element.get_attribute("placeholder")
        assert search_input_text == self.wp_lib.sidebar_search_input_text

    def TestSearchButtonElementExistsVisible(self):
        """
        Verify that the sidebar search button exists and is visible
        """
        search_button = self.wp_sidebar.sidebar_search_button_element
        assert search_button is not None
        assert search_button.is_displayed()

    def TestRecentPostsWidgetExistsVisible(self):
        """
        Verify that the sidebar recent posts widget is present and visible
        """
        recent_posts_widget = self.wp_sidebar.sidebar_recent_posts_element
        assert recent_posts_widget is not None
        assert recent_posts_widget.is_displayed()

    def TestRecentPostsTitleExistsVisible(self):
        """
        Verify that the sidebar recent posts widget has a title
        """
        recent_posts_title = self.wp_sidebar.sidebar_recent_posts_title_element
        assert recent_posts_title is not None
        assert recent_posts_title.is_displayed()

    def TestRecentPostsTitleText(self):
        """
        Verify that the sidebar recent posts widget has the correct title text
        """
        recent_posts_title = self.wp_sidebar.sidebar_recent_posts_title_element
        assert recent_posts_title.text == self.wp_lib.sidebar_recent_posts_title_text

    def TestRecentPostsListExistsVisible(self):
        """
        Verify that the sidebar recent posts widget has a list of recent posts
        """
        recent_posts_list = self.wp_sidebar.sidebar_recent_posts_list_element
        assert recent_posts_list is not None
        assert recent_posts_list.is_displayed()

    def TestRecentPostsListItemsCount(self):
        """
        Verify that the sidebar recent posts widget contains five recent posts
        """
        recent_posts_list_items = self.wp_sidebar.sidebar_recent_posts_list_items_elements
        assert len(recent_posts_list_items) == 5

    def TestRecentCommentsWidgetExistsVisible(self):
        """
        Verify that the sidebar recent comments widget is present and visible
        """
        recent_comments_widget = self.wp_sidebar.sidebar_recent_comments_element
        assert recent_comments_widget is not None
        assert recent_comments_widget.is_displayed()

    def TestRecentCommentsTitleExistsVisible(self):
        """
        Verify that the sidebar recent comments widget has a title
        """
        recent_comments_title = self.wp_sidebar.sidebar_recent_comments_title_element
        assert recent_comments_title is not None
        assert recent_comments_title.is_displayed()

    def TestRecentCommentsTitleText(self):
        """
        Verify that the sidebar recent comments widget has the correct title text
        """
        recent_comments_title = self.wp_sidebar.sidebar_recent_comments_title_element
        assert recent_comments_title.text == self.wp_lib.sidebar_recent_comments_title_text

    def TestRecentCommentsListExistsVisible(self):
        """
        Verify that the sidebar recent comments widget has a list of recent comments
        """
        recent_comments_list = self.wp_sidebar.sidebar_recent_comments_list_element
        assert recent_comments_list is not None
        assert recent_comments_list.is_displayed()

    def TestRecentCommentsListItemsCount(self):
        """
        Verify that the sidebar recent comments widget contains at least one comment
        """
        recent_comments_list_items = self.wp_sidebar.sidebar_recent_comments_list_items_elements
        assert len(recent_comments_list_items) >= 1
