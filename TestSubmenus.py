from BaseTest import BaseTest
import WPHomepage
from selenium.webdriver.common.action_chains import ActionChains

# TestSubmenus
# Written by Angela Korra'ti
# Last updated 5/10/2019
#
# This class conducts tests against the menu dropdowns on the main menu of my test Wordpress site.


class TestSubmenus(BaseTest):
    wp_menu = None

    def set_wp_menu(self, wp_menu):
        """
        Setup function to set the class variable wp_menu used in child tests.
        """
        self.wp_menu = wp_menu

    def verify_home_submenu(self):
        """
        Verify all aspects of the Home submenu
        """
        # Verify that the Home submenu isn't visible by default
        home_submenu_element = self.wp_menu.home_submenu_element
        assert home_submenu_element is not None
        assert home_submenu_element.is_displayed() is False

        # Verify that the Home submenu becomes visible when you hover over Home
        self.ac.move_to_element(self.wp_menu.home_menu_element).perform()
        assert home_submenu_element.is_displayed()
        assert self.wp_menu.home_submenu_text == self.wp_lib.submenu_home['text']
        home_submenu_element.click()
        assert self.driver.current_url == self.wp_lib.submenu_home['link']

    def verify_books_submenu(self):
        """
        Verify all aspects of the Books submenu
        """
        # Verify that the Books submenu isn't visible by default
        books_submenu_element = self.wp_menu.books_submenu_element
        assert books_submenu_element is not None
        assert books_submenu_element.is_displayed() is False

        # Verify that the Books submenu becomes visible when you hover over Books
        books_menu_element = self.wp_menu.books_menu_element
        self.ac.move_to_element(books_menu_element).perform()
        assert books_submenu_element.is_displayed()

    def verify_faerie_submenu(self):
        """
        Verify the Faerie Blood item on the Books submenu
        """
        books_menu_element = self.wp_menu.books_menu_element
        self.ac.move_to_element(books_menu_element).perform()
        assert self.wp_menu.faerie_submenu_text == self.wp_lib.submenu_faerie['text']
        assert self.wp_menu.faerie_submenu_link == self.wp_lib.submenu_faerie['link']
        self.wp_menu.faerie_submenu_element.click()
        assert self.driver.current_url == self.wp_lib.submenu_faerie['link']

    def verify_bone_submenu(self):
        """
        Verify the Bone Walker item on the Books submenu
        """
        books_menu_element = self.wp_menu.books_menu_element
        self.ac.move_to_element(books_menu_element).perform()
        assert self.wp_menu.bone_submenu_text == self.wp_lib.submenu_bone['text']
        assert self.wp_menu.bone_submenu_link == self.wp_lib.submenu_bone['link']
        self.wp_menu.bone_submenu_element.click()
        assert self.driver.current_url == self.wp_lib.submenu_bone['link']

    def verify_valor_submenu(self):
        """
        Verify the Valor of the Healer item on the Books submenu
        """
        books_menu_element = self.wp_menu.books_menu_element
        self.ac.move_to_element(books_menu_element).perform()
        assert self.wp_menu.valor_submenu_text == self.wp_lib.submenu_valor['text']
        assert self.wp_menu.valor_submenu_link == self.wp_lib.submenu_valor['link']
        self.wp_menu.valor_submenu_element.click()
        assert self.driver.current_url == self.wp_lib.submenu_valor['link']

    def verify_vengeance_submenu(self):
        """
        Verify the Vengeance of the Hunter item on the Books submenu
        """
        books_menu_element = self.wp_menu.books_menu_element
        self.ac.move_to_element(books_menu_element).perform()
        assert self.wp_menu.vengeance_submenu_text == self.wp_lib.submenu_vengeance['text']
        assert self.wp_menu.vengeance_submenu_link == self.wp_lib.submenu_vengeance['link']
        self.wp_menu.vengeance_submenu_element.click()
        assert self.driver.current_url == self.wp_lib.submenu_vengeance['link']

    def verify_victory_submenu(self):
        """
        Verify the Victory of the Hawk item on the Books submenu
        """
        books_menu_element = self.wp_menu.books_menu_element
        self.ac.move_to_element(books_menu_element).perform()
        assert self.wp_menu.victory_submenu_text == self.wp_lib.submenu_victory['text']
        assert self.wp_menu.victory_submenu_link == self.wp_lib.submenu_victory['link']
        self.wp_menu.victory_submenu_element.click()
        assert self.driver.current_url == self.wp_lib.submenu_victory['link']

    def verify_short_submenu(self):
        """
        Verify the Short Stories item on the Books submenu
        """
        books_menu_element = self.wp_menu.books_menu_element
        self.ac.move_to_element(books_menu_element).perform()
        assert self.wp_menu.short_submenu_text == self.wp_lib.submenu_short['text']
        assert self.wp_menu.short_submenu_link == self.wp_lib.submenu_short['link']
        self.wp_menu.short_submenu_element.click()
        assert self.driver.current_url == self.wp_lib.submenu_short['link']

    def verify_store_submenu(self):
        """
        Verify the Store submenu
        """
        store_submenu_element = self.wp_menu.store_submenu_element
        assert store_submenu_element is not None
        assert store_submenu_element.is_displayed() is False
        store_menu_element = self.wp_menu.store_menu_element
        self.ac.move_to_element(store_menu_element).perform()
        assert store_submenu_element.is_displayed()
        assert self.wp_menu.store_submenu_text == self.wp_lib.submenu_store['text']
        assert self.wp_menu.store_submenu_link == self.wp_lib.submenu_store['link']
        store_submenu_element.click()
        assert self.driver.current_url == self.wp_lib.submenu_store['link']
