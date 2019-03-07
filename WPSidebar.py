# WPSidebar
# Written by Angela Korra'ti
# Last updated 2/22/2019
#
# This is a helper class to define the layout of the sidebar. Used in turn by page level classes.


class WPSidebar:
    driver = None
    wp_lib = None

    def __init__(self, driver, wp_lib):
        """
        Init method for the class
        :param driver: Webdriver object to use
        :param wp_lib: Instance of WPTestLib support class for ids, classes, xpaths, etc.
        """
        self.driver = driver
        self.wp_lib = wp_lib

    @property
    def sidebar_search_element(self):
        """
        :return: Webdriver element pointing at the search widget
        """
        return self.driver.find_element_by_id(self.wp_lib.sidebar_search_id)

    @property
    def sidebar_search_input_element(self):
        """
        :return: Webdriver element pointing at the search input box
        """
        return self.driver.find_element_by_xpath(self.wp_lib.sidebar_search_input_xpath)

    @property
    def sidebar_search_button_element(self):
        """
        :return: Webdriver element pointing at the search button
        """
        return self.driver.find_element_by_xpath(self.wp_lib.sidebar_search_button_xpath)

    @property
    def sidebar_recent_posts_element(self):
        """
        :return: Webdriver element pointing at the recent posts widget
        """
        return self.driver.find_element_by_id(self.wp_lib.sidebar_recent_posts_id)

    @property
    def sidebar_recent_posts_title_element(self):
        """
        :return: Webdriver element pointing at the recent posts title
        """
        return self.driver.find_element_by_xpath(self.wp_lib.sidebar_recent_posts_title_xpath)

    @property
    def sidebar_recent_posts_title_text(self):
        """
        :return: Text from the recent posts title element
        """
        return self.sidebar_recent_posts_title_element.text

    @property
    def sidebar_recent_posts_list_element(self):
        """
        :return: Webdriver element pointing at the list of recent posts
        """
        return self.driver.find_element_by_xpath(self.wp_lib.sidebar_recent_posts_list_xpath)

    @property
    def sidebar_recent_posts_list_items_elements(self):
        """
        :return: List of webdriver elements pointing at the recent post links
        """
        return self.driver.find_elements_by_xpath(self.wp_lib.sidebar_recent_posts_list_xpath + "/li")

    @property
    def sidebar_recent_comments_element(self):
        """
        :return: Webdriver element pointing at the recent comments widget
        """
        return self.driver.find_element_by_id(self.wp_lib.sidebar_recent_comments_id)

    @property
    def sidebar_recent_comments_title_element(self):
        """
        :return: Webdriver element pointing at the recent comments title
        """
        return self.driver.find_element_by_xpath(self.wp_lib.sidebar_recent_comments_title_xpath)

    @property
    def sidebar_recent_comments_title_text(self):
        """
        :return: Text from the recent comments title element
        """
        return self.sidebar_recent_comments_title_element.text

    @property
    def sidebar_recent_comments_list_element(self):
        """
        :return: Webdriver element pointing at the list of recent comments
        """
        return self.driver.find_element_by_xpath(self.wp_lib.sidebar_recent_comments_list_xpath)

    @property
    def sidebar_recent_comments_list_items_elements(self):
        """
        :return: List of webdriver elements pointing at the recent comment links
        """
        return self.driver.find_elements_by_xpath(self.wp_lib.sidebar_recent_comments_list_xpath + "/li")

    @property
    def sidebar_archives_element(self):
        """
        :return: Webdriver element pointing at the archives widget
        """
        return self.driver.find_element_by_id(self.wp_lib.sidebar_archives_id)

    @property
    def sidebar_archives_title_element(self):
        """
        :return: Webdriver element pointing at the archives title
        """
        return self.driver.find_element_by_xpath(self.wp_lib.sidebar_archives_title_xpath)

    @property
    def sidebar_archives_title_text(self):
        """
        :return: Text from the archives title element
        """
        return self.sidebar_archives_title_element.text

    @property
    def sidebar_archives_list_element(self):
        """
        :return: Webdriver element pointing at the list of archives
        """
        return self.driver.find_element_by_xpath(self.wp_lib.sidebar_archives_list_xpath)

    @property
    def sidebar_archives_list_items_elements(self):
        """
        :return: List of webdriver elements pointing at the archives links
        """
        return self.driver.find_elements_by_xpath(self.wp_lib.sidebar_archives_list_xpath + "/li")

    @property
    def sidebar_categories_element(self):
        """
        :return: Webdriver element pointing at the categories widget
        """
        return self.driver.find_element_by_id(self.wp_lib.sidebar_categories_id)

    @property
    def sidebar_categories_title_element(self):
        """
        :return: Webdriver element pointing at the categories title
        """
        return self.driver.find_element_by_xpath(self.wp_lib.sidebar_categories_title_xpath)

    @property
    def sidebar_categories_title_text(self):
        """
        :return: Text from the categories title element
        """
        return self.sidebar_categories_title_element.text

    @property
    def sidebar_categories_list_element(self):
        """
        :return: Webdriver element pointing at the list of categories
        """
        return self.driver.find_element_by_xpath(self.wp_lib.sidebar_categories_list_xpath)

    @property
    def sidebar_categories_list_items_elements(self):
        """
        :return: List of webdriver elements pointing at the categories links
        """
        return self.driver.find_elements_by_xpath(self.wp_lib.sidebar_categories_list_xpath + "/li")

    @property
    def sidebar_meta_element(self):
        """
        :return: Webdriver element pointing at the meta widget
        """
        return self.driver.find_element_by_id(self.wp_lib.sidebar_meta_id)

    @property
    def sidebar_meta_title_element(self):
        """
        :return: Webdriver element pointing at the meta title
        """
        return self.driver.find_element_by_xpath(self.wp_lib.sidebar_meta_title_xpath)

    @property
    def sidebar_meta_title_text(self):
        """
        :return: Text from the meta title element
        """
        return self.sidebar_meta_title_element.text

    @property
    def sidebar_meta_list_element(self):
        """
        :return: Webdriver element pointing at the list of meta links
        """
        return self.driver.find_element_by_xpath(self.wp_lib.sidebar_meta_list_xpath)

    @property
    def sidebar_meta_list_items_elements(self):
        """
        :return: List of webdriver elements pointing at the meta links
        """
        return self.driver.find_elements_by_xpath(self.wp_lib.sidebar_meta_list_xpath + "/li")
