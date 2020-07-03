from BaseTest import BaseTest
import WPHomepage

# TestSidebar
# Written by Angela Korra'ti
# Last updated 2/22/2019
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
        assert self.wp_sidebar.sidebar_recent_posts_title_text == self.wp_lib.sidebar_recent_posts_title_text

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
        assert self.wp_sidebar.sidebar_recent_comments_title_text == self.wp_lib.sidebar_recent_comments_title_text

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

    def TestArchivesWidgetExistsVisible(self):
        """
        Verify that the sidebar archives widget is present and visible
        """
        archives_widget = self.wp_sidebar.sidebar_archives_element
        assert archives_widget is not None
        assert archives_widget.is_displayed()

    def TestArchivesTitleExistsVisible(self):
        """
        Verify that the sidebar archives widget has a title
        """
        archives_title = self.wp_sidebar.sidebar_archives_title_element
        assert archives_title is not None
        assert archives_title.is_displayed()

    def TestArchivesTitleText(self):
        """
        Verify that the sidebar archives widget has the correct title text
        """
        assert self.wp_sidebar.sidebar_archives_title_text == self.wp_lib.sidebar_archives_title_text

    def TestArchivesListExistsVisible(self):
        """
        Verify that the sidebar archives widget has a list of archives
        """
        archives_list = self.wp_sidebar.sidebar_archives_list_element
        assert archives_list is not None
        assert archives_list.is_displayed()

    def TestArchivesListItemsCount(self):
        """
        Verify that the sidebar archives widget contains at least one archive
        """
        archives_list_items = self.wp_sidebar.sidebar_archives_list_items_elements
        assert len(archives_list_items) >= 1

    def TestCategoriesWidgetExistsVisible(self):
        """
        Verify that the sidebar categories widget is present and visible
        """
        categories_widget = self.wp_sidebar.sidebar_categories_element
        assert categories_widget is not None
        assert categories_widget.is_displayed()

    def TestCategoriesTitleExistsVisible(self):
        """
        Verify that the sidebar categories widget has a title
        """
        categories_title = self.wp_sidebar.sidebar_categories_title_element
        assert categories_title is not None
        assert categories_title.is_displayed()

    def TestCategoriesTitleText(self):
        """
        Verify that the sidebar categories widget has the correct title text
        """
        assert self.wp_sidebar.sidebar_categories_title_text == self.wp_lib.sidebar_categories_title_text

    def TestCategoriesListExistsVisible(self):
        """
        Verify that the sidebar categories widget has a list of categories
        """
        categories_list = self.wp_sidebar.sidebar_categories_list_element
        assert categories_list is not None
        assert categories_list.is_displayed()

    def TestCategoriesListItemsCount(self):
        """
        Verify that the sidebar categories widget contains at least one category
        """
        categories_list_items = self.wp_sidebar.sidebar_categories_list_items_elements
        assert len(categories_list_items) >= 1

    def TestMetaWidgetExistsVisible(self):
        """
        Verify that the sidebar meta widget is present and visible
        """
        meta_widget = self.wp_sidebar.sidebar_meta_element
        assert meta_widget is not None
        assert meta_widget.is_displayed()

    def TestMetaTitleExistsVisible(self):
        """
        Verify that the sidebar categories meta has a title
        """
        meta_title = self.wp_sidebar.sidebar_meta_title_element
        assert meta_title is not None
        assert meta_title.is_displayed()

    def TestMetaTitleText(self):
        """
        Verify that the sidebar meta widget has the correct title text
        """
        assert self.wp_sidebar.sidebar_meta_title_text == self.wp_lib.sidebar_meta_title_text

    def TestMetaListExistsVisible(self):
        """
        Verify that the sidebar meta widget has a list of categories
        """
        meta_list = self.wp_sidebar.sidebar_meta_list_element
        assert meta_list is not None
        assert meta_list.is_displayed()

    def TestMetaListItemsCount(self):
        """
        Verify that the sidebar meta widget contains the correct number of meta links
        """
        meta_list_items = self.wp_sidebar.sidebar_meta_list_items_elements
        assert len(meta_list_items) == 4
