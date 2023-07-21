import WPPost
import pytest

# TestPostSearch
# Written by Angela Korra'ti
# Last updated 7/21/2023
#
# This class conducts search tests against my test WordPress site.


@pytest.mark.usefixtures("setup_webdriver", "wp_lib")
class TestPostSearch:
    wp_sidebar = None

    def setup_method(self):
        """
        Do setup for the test cases.
        """
        self.driver.get(self.wp_lib.wp_post_uri)
        self.wp_sidebar = WPPost.WPPost(self.driver, self.wp_lib).wp_sidebar

    def test_search_faerie_blood_enter(self):
        """
        Verify searching for 'Faerie Blood' and pressing Enter works as expected on the homepage
        """
        self.wp_sidebar.verify_search_faerie_blood_enter()

    def test_search_faerie_blood_click(self):
        """
        Verify searching for 'Faerie Blood' and clicking search button works as expected on the homepage
        """
        self.wp_sidebar.verify_search_faerie_blood_click()

    def test_search_wards_enter(self):
        """
        Verify searching for 'Walk the Wards' and pressing Enter works as expected on the homepage
        """
        self.wp_sidebar.verify_search_wards_enter()

    def test_search_wards_click(self):
        """
        Verify searching for 'Walk the Wards' and clicking search button works as expected on the homepage
        """
        self.wp_sidebar.verify_search_wards_click()
