from BaseTest import BaseTest
import WPHomepage
from selenium.webdriver.common.action_chains import ActionChains

# TestSubmenus
# Written by Angela Korra'ti
# Last updated 2/11/2019
#
# This class conducts tests against the menu dropdowns on the main menu of my test Wordpress site.


class TestSubmenus(BaseTest):
    wp_homepage = None
    wp_menu = None
    ac = None

    def setUp(self):
        """
        Do setup for the test cases.
        """
        super().setUp()
        self.driver.get(self.wp_lib.wp_base_uri)
        self.wp_homepage = WPHomepage.WPHomepage(self.driver, self.wp_lib)
        self.wp_menu = self.wp_homepage.wp_menu

    def TestHomeSubmenuNotVisible(self):
        """
        Verify that the Home submenu isn't visible by default
        """
        home_submenu_element = self.wp_menu.home_submenu_element
        assert home_submenu_element is not None
        assert home_submenu_element.is_displayed() is False

    def TestHomeSubmenuVisibleOnHover(self):
        """
        Verify that the Home submenu becomes visible when you hover over Home
        """
        home_menu_element = self.wp_menu.home_menu_element
        hover = ActionChains(self.driver).move_to_element(home_menu_element)
        hover.perform()
        home_submenu_element = self.wp_menu.home_submenu_element
        assert home_submenu_element is not None
        assert home_submenu_element.is_displayed()

    def TestHomeSubmenuText(self):
        """
        Verify that the Home submenu has the correct text
        """
        # Because apparently I need to do a hover first before I can see the text
        home_menu_element = self.wp_menu.home_menu_element
        hover = ActionChains(self.driver).move_to_element(home_menu_element)
        hover.perform()
        assert self.wp_menu.home_submenu_text == self.wp_lib.submenu_home['text']

    def TestHomeSubmenuLink(self):
        """
        Verify that the Home submenu has the correct link
        """
        assert self.wp_menu.home_submenu_link == self.wp_lib.submenu_home['link']

    def TestHomeSubmenuLinkClick(self):
        """
        Verify that clicking on the Home submenu link takes you to correct page (angelahighland.com)
        """
        home_menu_element = self.wp_menu.home_menu_element
        hover = ActionChains(self.driver).move_to_element(home_menu_element)
        hover.perform()
        home_submenu_element = self.wp_menu.home_submenu_element
        hover = ActionChains(self.driver).move_to_element(home_submenu_element)
        hover.perform()
        home_submenu_element.click()
        assert self.driver.current_url == self.wp_lib.submenu_home['link']