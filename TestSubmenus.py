from BaseTest import BaseTest
import WPHomepage
from selenium.webdriver.common.action_chains import ActionChains

# TestSubmenus
# Written by Angela Korra'ti
# Last updated 2/14/2019
#
# This class conducts tests against the menu dropdowns on the main menu of my test Wordpress site.


class TestSubmenus(BaseTest):
    wp_menu = None
    ac = None

    def setUp(self):
        """
        Do setup for the test cases.
        """
        super().setUp()
        self.driver.get(self.wp_lib.wp_base_uri)
        self.wp_menu = WPHomepage.WPHomepage(self.driver, self.wp_lib).wp_menu
        self.ac = ActionChains(self.driver)

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
        self.ac.move_to_element(home_menu_element).perform()
        home_submenu_element = self.wp_menu.home_submenu_element
        assert home_submenu_element is not None
        assert home_submenu_element.is_displayed()

    def TestHomeSubmenuText(self):
        """
        Verify that the Home submenu has the correct text
        """
        # Because apparently I need to do a hover first before I can see the text
        home_menu_element = self.wp_menu.home_menu_element
        self.ac.move_to_element(home_menu_element).perform()
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
        self.ac.move_to_element(home_menu_element).perform()
        home_submenu_element = self.wp_menu.home_submenu_element
        self.ac.move_to_element(home_submenu_element).perform()
        home_submenu_element.click()
        assert self.driver.current_url == self.wp_lib.submenu_home['link']

    def TestBooksSubmenuNotVisible(self):
        """
        Verify that the Books submenu isn't visible by default
        """
        books_submenu_element = self.wp_menu.books_submenu_element
        assert books_submenu_element is not None
        assert books_submenu_element.is_displayed() is False

    def TestBooksSubmenuVisibleOnHover(self):
        """
        Verify that the Books submenu becomes visible when you hover over Books
        """
        books_menu_element = self.wp_menu.books_menu_element
        self.ac.move_to_element(books_menu_element).perform()
        books_submenu_element = self.wp_menu.books_submenu_element
        assert books_submenu_element is not None
        assert books_submenu_element.is_displayed()

    def TestFaerieSubmenuText(self):
        """
        Verify that the Faerie Blood item on the Books submenu has the correct text
        """
        books_menu_element = self.wp_menu.books_menu_element
        self.ac.move_to_element(books_menu_element).perform()
        assert self.wp_menu.faerie_submenu_text == self.wp_lib.submenu_faerie['text']

    def TestFaerieSubmenuLink(self):
        """
        Verify that the Faerie Blood item on the Books submenu has the correct link
        """
        assert self.wp_menu.faerie_submenu_link == self.wp_lib.submenu_faerie['link']

    def TestFaerieSubmenuLinkClick(self):
        """
        Verify that clicking the Faerie Blood item on the Books submenu takes you to the correct page
        """
        books_menu_element = self.wp_menu.books_menu_element
        self.ac.move_to_element(books_menu_element).perform()
        self.wp_menu.faerie_submenu_element.click()
        assert self.driver.current_url == self.wp_lib.submenu_faerie['link']

    def TestBoneSubmenuText(self):
        """
        Verify that the Bone Walker item on the Books submenu has the correct text
        """
        books_menu_element = self.wp_menu.books_menu_element
        self.ac.move_to_element(books_menu_element).perform()
        assert self.wp_menu.bone_submenu_text == self.wp_lib.submenu_bone['text']

    def TestBoneSubmenuLink(self):
        """
        Verify that the Bone Walker item on the Books submenu has the correct link
        """
        assert self.wp_menu.bone_submenu_link == self.wp_lib.submenu_bone['link']

    def TestBoneSubmenuLinkClick(self):
        """
        Verify that clicking the Bone Walker item on the Books submenu takes you to the correct page
        """
        books_menu_element = self.wp_menu.books_menu_element
        self.ac.move_to_element(books_menu_element).perform()
        self.wp_menu.bone_submenu_element.click()
        assert self.driver.current_url == self.wp_lib.submenu_bone['link']

    def TestValorSubmenuText(self):
        """
        Verify that the Valor of the Healer item on the Books submenu has the correct text
        """
        books_menu_element = self.wp_menu.books_menu_element
        self.ac.move_to_element(books_menu_element).perform()
        assert self.wp_menu.valor_submenu_text == self.wp_lib.submenu_valor['text']

    def TestValorSubmenuLink(self):
        """
        Verify that the Valor of the Healer item on the Books submenu has the correct link
        """
        assert self.wp_menu.valor_submenu_link == self.wp_lib.submenu_valor['link']

    def TestValorSubmenuLinkClick(self):
        """
        Verify that clicking the Valor of the Healer item on the Books submenu takes you to the correct page
        """
        books_menu_element = self.wp_menu.books_menu_element
        self.ac.move_to_element(books_menu_element).perform()
        self.wp_menu.valor_submenu_element.click()
        assert self.driver.current_url == self.wp_lib.submenu_valor['link']

    def TestVengeanceSubmenuText(self):
        """
        Verify that the Vengeance of the Hunter item on the Books submenu has the correct text
        """
        books_menu_element = self.wp_menu.books_menu_element
        self.ac.move_to_element(books_menu_element).perform()
        assert self.wp_menu.vengeance_submenu_text == self.wp_lib.submenu_vengeance['text']

    def TestVengeanceSubmenuLink(self):
        """
        Verify that the Vengeance of the Hunter item on the Books submenu has the correct link
        """
        assert self.wp_menu.vengeance_submenu_link == self.wp_lib.submenu_vengeance['link']

    def TestVengeanceSubmenuLinkClick(self):
        """
        Verify that clicking the Vengeance of the Hunter item on the Books submenu takes you to the correct page
        """
        books_menu_element = self.wp_menu.books_menu_element
        self.ac.move_to_element(books_menu_element).perform()
        self.wp_menu.vengeance_submenu_element.click()
        assert self.driver.current_url == self.wp_lib.submenu_vengeance['link']

    def TestVictorySubmenuText(self):
        """
        Verify that the Victory of the Hawk item on the Books submenu has the correct text
        """
        books_menu_element = self.wp_menu.books_menu_element
        self.ac.move_to_element(books_menu_element).perform()
        assert self.wp_menu.victory_submenu_text == self.wp_lib.submenu_victory['text']

    def TestVictorySubmenuLink(self):
        """
        Verify that the Victory of the Hawk item on the Books submenu has the correct link
        """
        assert self.wp_menu.victory_submenu_link == self.wp_lib.submenu_victory['link']

    def TestVictorySubmenuLinkClick(self):
        """
        Verify that clicking the Victory of the Hawk item on the Books submenu takes you to the correct page
        """
        books_menu_element = self.wp_menu.books_menu_element
        self.ac.move_to_element(books_menu_element).perform()
        self.wp_menu.victory_submenu_element.click()
        assert self.driver.current_url == self.wp_lib.submenu_victory['link']

    def TestShortSubmenuText(self):
        """
        Verify that the Short Stories item on the Books submenu has the correct text
        """
        books_menu_element = self.wp_menu.books_menu_element
        self.ac.move_to_element(books_menu_element).perform()
        assert self.wp_menu.short_submenu_text == self.wp_lib.submenu_short['text']

    def TestShortSubmenuLink(self):
        """
        Verify that the Short Stories item on the Books submenu has the correct link
        """
        assert self.wp_menu.short_submenu_link == self.wp_lib.submenu_short['link']

    def TestShortSubmenuLinkClick(self):
        """
        Verify that clicking the Short Stories item on the Books submenu takes you to the correct page
        """
        books_menu_element = self.wp_menu.books_menu_element
        self.ac.move_to_element(books_menu_element).perform()
        self.wp_menu.short_submenu_element.click()
        assert self.driver.current_url == self.wp_lib.submenu_short['link']

    def TestStoreSubmenuNotVisible(self):
        """
        Verify that the Store submenu isn't visible by default
        """
        store_submenu_element = self.wp_menu.store_submenu_element
        assert store_submenu_element is not None
        assert store_submenu_element.is_displayed() is False

    def TestStoreSubmenuVisibleOnHover(self):
        """
        Verify that the Store submenu becomes visible when you hover over Store
        """
        store_menu_element = self.wp_menu.store_menu_element
        self.ac.move_to_element(store_menu_element).perform()
        store_submenu_element = self.wp_menu.store_submenu_element
        assert store_submenu_element is not None
        assert store_submenu_element.is_displayed()

    def TestStoreSubmenuText(self):
        """
        Verify that the Store submenu has the correct text
        """
        # Because apparently I need to do a hover first before I can see the text
        store_menu_element = self.wp_menu.store_menu_element
        self.ac.move_to_element(store_menu_element).perform()
        assert self.wp_menu.store_submenu_text == self.wp_lib.submenu_store['text']

    def TestStoreSubmenuLink(self):
        """
        Verify that the Store submenu has the correct link
        """
        assert self.wp_menu.store_submenu_link == self.wp_lib.submenu_store['link']

    def TestStoreSubmenuLinkClick(self):
        """
        Verify that clicking on the Store submenu link takes you to correct page (Square store)
        """
        store_menu_element = self.wp_menu.store_menu_element
        self.ac.move_to_element(store_menu_element).perform()
        store_submenu_element = self.wp_menu.store_submenu_element
        self.ac.move_to_element(store_submenu_element).perform()
        store_submenu_element.click()
        assert self.driver.current_url == self.wp_lib.submenu_store['link']
