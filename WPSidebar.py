from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import WPPost
from selenium.webdriver.common.keys import Keys

# WPSidebar
# Written by Angela Korra'ti
# Last updated 7/19/2023
#
# This is a helper class to define the layout of the sidebar. Used in turn by page level classes.


class WPSidebar:
    driver = None
    wp_lib = None
    ac = None

    # Strings pertaining to the sidebar
    sidebar_search_id = "search-2"
    sidebar_search_input_xpath = "//*[@id='search-2']/form/label/input"
    sidebar_search_input_text = "Search \u2026"
    sidebar_search_button_xpath = "//*[@id='search-2']/form/button"
    sidebar_recent_posts_id = "recent-posts-2"
    sidebar_recent_posts_title_xpath = "//*[@id='recent-posts-2']/h2"
    sidebar_recent_posts_title_text = "RECENT POSTS"
    sidebar_recent_posts_list_xpath = "//*[@id='recent-posts-2']/*/ul"
    sidebar_recent_comments_id = "recent-comments-2"
    sidebar_recent_comments_title_xpath = "//*[@id='recent-comments-2']/h2"
    sidebar_recent_comments_title_text = "RECENT COMMENTS"
    sidebar_recent_comments_list_xpath = "//*[@id='recent-comments-2']/*/ul"
    sidebar_archives_id = "archives-2"
    sidebar_archives_title_xpath = "//*[@id='archives-2']/h2"
    sidebar_archives_title_text = "ARCHIVES"
    sidebar_archives_list_xpath = "//*[@id='archives-2']/*/ul"
    sidebar_categories_id = "categories-2"
    sidebar_categories_title_xpath = "//*[@id='categories-2']/h2"
    sidebar_categories_title_text = "CATEGORIES"
    sidebar_categories_list_xpath = "//*[@id='categories-2']/*/ul"
    sidebar_meta_id = "meta-2"
    sidebar_meta_title_xpath = "//*[@id='meta-2']/h2"
    sidebar_meta_title_text = "META"
    sidebar_meta_list_xpath = "//*[@id='meta-2']/*/ul"

    # Strings pertaining to search
    search_string = "Faerie Blood"
    search_uri = "?s=Faerie+Blood"
    search_results_string = "Search Results for: "
    search_no_results_string = "Walk the Wards"
    search_no_results_uri = "?s=Walk+the+Wards"
    search_no_results_message = "Nothing Found"

    # Strings pertaining to testing clicking on Recent Posts
    recent_posts_uri = "2017/04/17/angelahighland-info-domain-now-active/"
    recent_posts_title = "angelahighland.info domain now active"

    # Strings pertaining to testing clicking on Recent Comments
    recent_comments_uri = "2016/09/12/hello-readers/#comment-"
    recent_comments_title = "Hello, readers!"

    # Strings pertaining to testing clicking on Archives
    archives_uri = "2017/04/"
    archives_string = "Month: "
    archives_title = "April 2017"

    # Strings pertaining to testing clicking on Categories
    categories_uri = "category/about-me/"
    categories_string = "Category: "
    categories_title = "About Me"

    # Strings pertaining to testing clicking on Meta links
    meta_login_uri = "wp-login.php"

    def __init__(self, driver, wp_lib):
        """
        Init method for the class
        :param driver: Webdriver object to use
        :param wp_lib: WPLib object to use
        """
        self.driver = driver
        self.wp_lib = wp_lib
        self.ac = ActionChains(self.driver)

    @property
    def search_element(self):
        """
        :return: Webdriver element pointing at the search widget
        """
        return self.driver.find_element(By.ID, self.sidebar_search_id)

    @property
    def search_input_element(self):
        """
        :return: Webdriver element pointing at the search input box
        """
        return self.driver.find_element(By.XPATH, self.sidebar_search_input_xpath)

    @property
    def search_button_element(self):
        """
        :return: Webdriver element pointing at the search button
        """
        return self.driver.find_element(By.XPATH, self.sidebar_search_button_xpath)

    @property
    def recent_posts_element(self):
        """
        :return: Webdriver element pointing at the recent posts widget
        """
        return self.driver.find_element(By.ID, self.sidebar_recent_posts_id)

    @property
    def recent_posts_title_element(self):
        """
        :return: Webdriver element pointing at the recent posts title
        """
        return self.driver.find_element(By.XPATH, self.sidebar_recent_posts_title_xpath)

    @property
    def recent_posts_title_text(self):
        """
        :return: Text from the recent posts title element
        """
        return self.recent_posts_title_element.text

    @property
    def recent_posts_list_element(self):
        """
        :return: Webdriver element pointing at the list of recent posts
        """
        return self.driver.find_element(By.XPATH, self.sidebar_recent_posts_list_xpath)

    @property
    def recent_posts_list_elements(self):
        """
        :return: List of webdriver elements pointing at the recent post links
        """
        return self.driver.find_elements(By.XPATH, self.sidebar_recent_posts_list_xpath + "/li/a")

    @property
    def recent_comments_element(self):
        """
        :return: Webdriver element pointing at the recent comments widget
        """
        return self.driver.find_element(By.ID, self.sidebar_recent_comments_id)

    @property
    def recent_comments_title_element(self):
        """
        :return: Webdriver element pointing at the recent comments title
        """
        return self.driver.find_element(By.XPATH, self.sidebar_recent_comments_title_xpath)

    @property
    def recent_comments_title_text(self):
        """
        :return: Text from the recent comments title element
        """
        return self.recent_comments_title_element.text

    @property
    def recent_comments_list_element(self):
        """
        :return: Webdriver element pointing at the list of recent comments
        """
        return self.driver.find_element(By.XPATH, self.sidebar_recent_comments_list_xpath)

    @property
    def recent_comments_list_elements(self):
        """
        :return: List of webdriver elements pointing at the recent comment links
        """
        return self.driver.find_elements(By.XPATH, self.sidebar_recent_comments_list_xpath + "/li/a")

    @property
    def archives_element(self):
        """
        :return: Webdriver element pointing at the archives widget
        """
        return self.driver.find_element(By.ID, self.sidebar_archives_id)

    @property
    def archives_title_element(self):
        """
        :return: Webdriver element pointing at the archives title
        """
        return self.driver.find_element(By.XPATH, self.sidebar_archives_title_xpath)

    @property
    def archives_title_text(self):
        """
        :return: Text from the archives title element
        """
        return self.archives_title_element.text

    @property
    def archives_list_element(self):
        """
        :return: Webdriver element pointing at the list of archives
        """
        return self.driver.find_element(By.XPATH, self.sidebar_archives_list_xpath)

    @property
    def archives_list_elements(self):
        """
        :return: List of webdriver elements pointing at the archives links
        """
        return self.driver.find_elements(By.XPATH, self.sidebar_archives_list_xpath + "/li/a")

    @property
    def categories_element(self):
        """
        :return: Webdriver element pointing at the categories widget
        """
        return self.driver.find_element(By.ID, self.sidebar_categories_id)

    @property
    def categories_title_element(self):
        """
        :return: Webdriver element pointing at the categories title
        """
        return self.driver.find_element(By.XPATH, self.sidebar_categories_title_xpath)

    @property
    def categories_title_text(self):
        """
        :return: Text from the categories title element
        """
        return self.categories_title_element.text

    @property
    def categories_list_element(self):
        """
        :return: Webdriver element pointing at the list of categories
        """
        return self.driver.find_element(By.XPATH, self.sidebar_categories_list_xpath)

    @property
    def categories_list_elements(self):
        """
        :return: List of webdriver elements pointing at the categories links
        """
        return self.driver.find_elements(By.XPATH, self.sidebar_categories_list_xpath + "/li/a")

    @property
    def meta_element(self):
        """
        :return: Webdriver element pointing at the meta widget
        """
        return self.driver.find_element(By.ID, self.sidebar_meta_id)

    @property
    def meta_title_element(self):
        """
        :return: Webdriver element pointing at the meta title
        """
        return self.driver.find_element(By.XPATH, self.sidebar_meta_title_xpath)

    @property
    def meta_title_text(self):
        """
        :return: Text from the meta title element
        """
        return self.meta_title_element.text

    @property
    def meta_list_element(self):
        """
        :return: Webdriver element pointing at the list of meta links
        """
        return self.driver.find_element(By.XPATH, self.sidebar_meta_list_xpath)

    @property
    def meta_list_elements(self):
        """
        :return: List of webdriver elements pointing at the meta links
        """
        return self.driver.find_elements(By.XPATH, self.sidebar_meta_list_xpath + "/li/a")

    def verify_search_widget(self):
        """
        Verify that the sidebar search widget is present and visible
        """
        assert self.search_element is not None
        assert self.search_element.is_displayed()

    def verify_search_input(self):
        """
        Verify that the sidebar search input box is present and visible and has the expected text
        """
        assert self.search_input_element is not None
        assert self.search_input_element.is_displayed()
        assert self.search_input_element.get_attribute("placeholder") == self.sidebar_search_input_text

    def verify_search_button(self):
        """
        Verify that the sidebar search button exists and is visible
        """
        assert self.search_button_element is not None
        assert self.search_button_element.is_displayed()

    def verify_recent_posts(self):
        """
        Verify that the recent posts widget is present and visible, has the correct title, and has five posts
        """
        assert self.recent_posts_element is not None
        assert self.recent_posts_element.is_displayed()
        assert self.recent_posts_title_element is not None
        assert self.recent_posts_title_element.is_displayed()
        assert self.recent_posts_title_text == self.sidebar_recent_posts_title_text
        assert self.recent_posts_list_element is not None
        assert self.recent_posts_list_element.is_displayed()
        assert len(self.recent_posts_list_elements) == 5

    def verify_recent_comments(self):
        """
        Verify the recent comments widget is present and visible, and has the correct title and comment count
        """
        assert self.recent_comments_element is not None
        assert self.recent_comments_element.is_displayed()
        assert self.recent_comments_title_element is not None
        assert self.recent_comments_title_element.is_displayed()
        assert self.recent_comments_title_text == self.sidebar_recent_comments_title_text
        assert self.recent_comments_list_element is not None
        assert self.recent_comments_list_element.is_displayed()
        assert len(self.recent_comments_list_elements) >= 1

    def verify_archives(self):
        """
        Verify the archives widget is present and visible, has the correct title, and has the correct count of links
        """
        assert self.archives_element is not None
        assert self.archives_element.is_displayed()
        assert self.archives_title_element is not None
        assert self.archives_title_element.is_displayed()
        assert self.archives_title_text == self.sidebar_archives_title_text
        assert self.archives_list_element is not None
        assert self.archives_list_element.is_displayed()
        assert len(self.archives_list_elements) >= 1

    def verify_categories(self):
        """
        Verify the categories widget is present and visible, has the correct title, and has the correct count of links
        """
        assert self.categories_element is not None
        assert self.categories_element.is_displayed()
        assert self.categories_title_element is not None
        assert self.categories_title_element.is_displayed()
        assert self.categories_title_text == self.sidebar_categories_title_text
        assert self.categories_list_element is not None
        assert self.categories_list_element.is_displayed()
        assert len(self.categories_list_elements) >= 1

    def verify_meta(self):
        """
        Verify that the meta widget is present and visible, has the correct title, and has the correct count of links
        """
        assert self.meta_element is not None
        assert self.meta_element.is_displayed()
        assert self.meta_title_element is not None
        assert self.meta_title_element.is_displayed()
        assert self.meta_title_text == self.sidebar_meta_title_text
        assert self.meta_list_element is not None
        assert self.meta_list_element.is_displayed()
        assert len(self.meta_list_elements) == 4

    def verify_recent_posts_link_click(self):
        """
        Verify clicking the first link in the Recent Posts links goes to the expected post
        """
        self.ac.move_to_element(self.search_element).perform()
        self.recent_posts_list_elements[0].click()
        assert self.driver.current_url == self.wp_lib.wp_base_uri + self.recent_posts_uri
        wp_post = WPPost.WPPost(self.driver, self.wp_lib)
        assert wp_post.post_title_element is not None
        assert wp_post.post_title_element.is_displayed()
        assert wp_post.post_title_text == self.recent_posts_title

    def verify_recent_comments_link_click(self):
        """
        Verify clicking the first link in the Recent Comments links goes to the expected comment
        """
        self.ac.move_to_element(self.recent_posts_list_elements[4]).perform()
        self.recent_comments_list_elements[0].click()

        # 7/7/2023 Looking for MOST of the URI here because the actual comment number changes
        # depending on when I last set up the test WordPress database, or if I had to import
        # multiple times
        most_of_uri = self.wp_lib.wp_base_uri + self.recent_comments_uri
        assert self.driver.current_url.startswith(most_of_uri)
        wp_post = WPPost.WPPost(self.driver, self.wp_lib)
        assert wp_post.post_title_element is not None
        assert wp_post.post_title_element.is_displayed()
        assert wp_post.post_title_text == self.recent_comments_title

    def verify_archives_link_click(self):
        """
        Verify clicking the first link in the Archives links goes to the expected archives page
        """
        self.ac.move_to_element(self.archives_element).perform()
        self.archives_list_elements[0].click()
        assert self.driver.current_url == self.wp_lib.wp_base_uri + self.archives_uri
        page_title = self.driver.find_element(By.CLASS_NAME, self.wp_lib.page_title_class)
        assert page_title is not None
        assert page_title.is_displayed()
        assert page_title.text == self.archives_string + self.archives_title

    def verify_categories_link_click(self):
        """
        Verify clicking the first link in the Categories links goes to the expected category page
        """
        self.ac.move_to_element(self.categories_element).perform()
        self.categories_list_elements[0].click()
        assert self.driver.current_url == self.wp_lib.wp_base_uri + self.categories_uri
        page_title = self.driver.find_element(By.CLASS_NAME, self.wp_lib.page_title_class)
        assert page_title is not None
        assert page_title.is_displayed()
        assert page_title.text == self.categories_string + self.categories_title

    def verify_meta_login_link_click(self):
        """
        Verify clicking on the first link in the Meta links goes to the login page
        """
        self.ac.move_to_element(self.meta_element).perform()
        self.meta_list_elements[0].click()
        assert self.driver.current_url == self.wp_lib.wp_base_uri + self.meta_login_uri
        self.driver.back()

    def verify_search_faerie_blood_enter(self):
        """
        Verify searching for 'Faerie Blood' and pressing Enter works as expected
        """
        # Do the search
        self.search_input_element.send_keys(self.search_string + Keys.RETURN)

        # Make sure we land on the correct URL
        assert self.driver.current_url == self.wp_lib.wp_base_uri + self.search_uri

        # Make sure the search string is appropriately reflected in the page title
        page_title = self.driver.find_element(By.CLASS_NAME, self.wp_lib.page_title_class)
        assert page_title is not None
        assert page_title.is_displayed()
        assert page_title.text == self.search_results_string + self.search_string

    def verify_search_faerie_blood_click(self):
        """
        Verify searching for 'Faerie Blood' and clicking search button works as expected
        """
        # Do the search
        self.search_input_element.send_keys(self.search_string)
        self.search_button_element.click()

        # Make sure we land on the correct URL
        assert self.driver.current_url == self.wp_lib.wp_base_uri + self.search_uri

        # Make sure the search string is appropriately reflected in the page title
        page_title = self.driver.find_element(By.CLASS_NAME, self.wp_lib.page_title_class)
        assert page_title is not None
        assert page_title.is_displayed()
        assert page_title.text == self.search_results_string + self.search_string

    def verify_search_wards_enter(self):
        """
        Verify searching for 'Walk the Wards' and pressing Enter works as expected
        """
        # Do the search
        self.search_input_element.send_keys(self.search_no_results_string + Keys.RETURN)

        # Make sure we land on the correct URL
        assert self.driver.current_url == self.wp_lib.wp_base_uri + self.search_no_results_uri

        # Make sure the search string is appropriately reflected in the page title
        page_title = self.driver.find_element(By.CLASS_NAME, self.wp_lib.page_title_class)
        assert page_title is not None
        assert page_title.is_displayed()
        assert page_title.text == self.search_no_results_message

    def verify_search_wards_click(self):
        """
        Verify searching for 'Walk the Wards' and clicking search button works as expected
        """
        # Do the search
        self.search_input_element.send_keys(self.search_no_results_string)
        self.search_button_element.click()

        # Make sure we land on the correct URL
        assert self.driver.current_url == self.wp_lib.wp_base_uri + self.search_no_results_uri

        # Make sure the search string is appropriately reflected in the page title
        page_title = self.driver.find_element(By.CLASS_NAME, self.wp_lib.page_title_class)
        assert page_title is not None
        assert page_title.is_displayed()
        assert page_title.text == self.search_no_results_message
