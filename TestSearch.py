from selenium.webdriver.common.keys import Keys
from BaseTest import BaseTest
import WPHomepage

# TestSearch
# Written by Angela Korra'ti
# Last updated 2/22/2019
#
# This class conducts search tests against my test Wordpress site.


class TestSearch(BaseTest):
    wp_sidebar = None

    def setUp(self):
        """
        Do setup for the test cases.
        """
        super().setUp()
        self.driver.get(self.wp_lib.wp_base_uri)
        self.wp_sidebar = WPHomepage.WPHomepage(self.driver, self.wp_lib).wp_sidebar

    def TestSearchForFaerieBloodPressEnter(self):
        """
        Verify searching for 'Faerie Blood' and pressing Enter works as expected
        """
        # Do the search
        search_input = self.wp_sidebar.sidebar_search_input_element
        search_input.send_keys(self.wp_lib.search_string + Keys.RETURN)

        # Make sure we land on the correct URL
        assert self.driver.current_url == self.wp_lib.wp_base_uri + self.wp_lib.search_uri

        # Make sure the search string is appropriately reflected in the page title
        page_title = self.driver.find_element_by_class_name(self.wp_lib.page_title_class)
        assert page_title is not None
        assert page_title.is_displayed()
        assert page_title.text == self.wp_lib.search_results_string + self.wp_lib.search_string

    def TestSearchForFaerieBloodClick(self):
        """
        Verify searching for 'Faerie Blood' and clicking search button works as expected
        """
        # Do the search
        search_input = self.wp_sidebar.sidebar_search_input_element
        search_input.send_keys(self.wp_lib.search_string)
        self.wp_sidebar.sidebar_search_button_element.click()

        # Make sure we land on the correct URL
        assert self.driver.current_url == self.wp_lib.wp_base_uri + self.wp_lib.search_uri

        # Make sure the search string is appropriately reflected in the page title
        page_title = self.driver.find_element_by_class_name(self.wp_lib.page_title_class)
        assert page_title is not None
        assert page_title.is_displayed()
        assert page_title.text == self.wp_lib.search_results_string + self.wp_lib.search_string

    def TestSearchForWalkTheWardsPressEnter(self):
        """
        Verify searching for 'Walk the Wards' and pressing Enter works as expected
        """
        # Do the search
        search_input = self.wp_sidebar.sidebar_search_input_element
        search_input.send_keys(self.wp_lib.search_no_results_string + Keys.RETURN)

        # Make sure we land on the correct URL
        assert self.driver.current_url == self.wp_lib.wp_base_uri + self.wp_lib.search_no_results_uri

        # Make sure the search string is appropriately reflected in the page title
        page_title = self.driver.find_element_by_class_name(self.wp_lib.page_title_class)
        assert page_title is not None
        assert page_title.is_displayed()
        assert page_title.text == self.wp_lib.search_no_results_message

    def TestSearchForWalkTheWardsClick(self):
        """
        Verify searching for 'Walk the Wards' and clicking search button works as expected
        """
        # Do the search
        search_input = self.wp_sidebar.sidebar_search_input_element
        search_input.send_keys(self.wp_lib.search_no_results_string)
        self.wp_sidebar.sidebar_search_button_element.click()

        # Make sure we land on the correct URL
        assert self.driver.current_url == self.wp_lib.wp_base_uri + self.wp_lib.search_no_results_uri

        # Make sure the search string is appropriately reflected in the page title
        page_title = self.driver.find_element_by_class_name(self.wp_lib.page_title_class)
        assert page_title is not None
        assert page_title.is_displayed()
        assert page_title.text == self.wp_lib.search_no_results_message