from TestSearch import TestSearch
import WPHomepage

# TestHomepageSearch
# Written by Angela Korra'ti
# Last updated 5/10/2019
#
# This class conducts search tests against my test WordPress site.


class TestHomepageSearch(TestSearch):
    wp_sidebar = None

    def setUp(self):
        """
        Do setup for the test cases.
        """
        super().setUp()
        self.driver.get(self.wp_lib.wp_base_uri)
        self.wp_sidebar = WPHomepage.WPHomepage(self.driver, self.wp_lib).wp_sidebar

    def test_search_faerie_blood_enter(self):
        """
        Verify searching for 'Faerie Blood' and pressing Enter works as expected on the homepage
        """
        self.verify_search_faerie_blood_enter()

    def test_search_faerie_blood_click(self):
        """
        Verify searching for 'Faerie Blood' and clicking search button works as expected on the homepage
        """
        self.verify_search_faerie_blood_enter()

    def test_search_wards_enter(self):
        """
        Verify searching for 'Walk the Wards' and pressing Enter works as expected
        """
        self.verify_search_wards_enter()

    def test_search_wards_click(self):
        """
        Verify searching for 'Walk the Wards' and clicking search button works as expected
        """
        # Do the search
        search_input = self.wp_sidebar.search_input_element
        search_input.send_keys(self.wp_lib.search_no_results_string)
        self.wp_sidebar.search_button_element.click()

        # Make sure we land on the correct URL
        assert self.driver.current_url == self.wp_lib.wp_base_uri + self.wp_lib.search_no_results_uri

        # Make sure the search string is appropriately reflected in the page title
        page_title = self.driver.find_element_by_class_name(self.wp_lib.page_title_class)
        assert page_title is not None
        assert page_title.is_displayed()
        assert page_title.text == self.wp_lib.search_no_results_message
