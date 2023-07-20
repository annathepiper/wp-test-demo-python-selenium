from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


# WPMenu
# Written by Angela Korra'ti
# Last updated 7/20/2023
#
# This is a helper class to define the layout of the main menu. Used in turn by page level classes.


class WPMenu:
    driver = None
    ac = None

    # These are all strings pertaining to primary menu items.
    menu_id = "menu-primary"
    menu_home = {"XPath": "//*[@id='menu-primary']/li[1]/a", "text": "Home", "link": "http://wordpress.local/"}
    menu_about = {"XPath": "//*[@id='menu-primary']/li[2]/a", "text": "About", "link": "http://wordpress.local/about/"}
    menu_books = {"XPath": "//*[@id='menu-primary']/li[3]/a", "text": "Books", "link": "http://wordpress.local/books/"}
    menu_blog = {"XPath": "//*[@id='menu-primary']/li[4]/a", "text": "Blog", "link": "http://wordpress.local/blog/"}
    menu_contact = {"XPath": "//*[@id='menu-primary']/li[5]/a", "text": "Contact",
                    "link": "http://wordpress.local/contact/"}
    menu_store = {"XPath": "//*[@id='menu-primary']/li[6]/a", "text": "Store",
                  "link": "https://angela-korrati.square.site/"}

    # Secondary menu items for the Home menu
    submenu_home = {"XPath": "//*[@id='menu-primary']/li[1]/ul/li/a", "text": "Angelahighland.com",
                    "link": "http://www.angelahighland.com/"}

    # Secondary menu items for the Books menu
    submenu_books_xpath = "//*[@id='menu-primary']/li[3]/ul"
    submenu_faerie = {"XPath": "//*[@id='menu-primary']/li[3]/ul/li[1]/a", "text": "Faerie Blood",
                      "link": "http://wordpress.local/books/faerie-blood/"}
    submenu_bone = {"XPath": "//*[@id='menu-primary']/li[3]/ul/li[2]/a", "text": "Bone Walker",
                    "link": "http://wordpress.local/books/bone-walker/"}
    submenu_valor = {"XPath": "//*[@id='menu-primary']/li[3]/ul/li[3]/a", "text": "Valor of the Healer",
                     "link": "http://wordpress.local/books/valor-of-the-healer/"}
    submenu_vengeance = {"XPath": "//*[@id='menu-primary']/li[3]/ul/li[4]/a", "text": "Vengeance of the Hunter",
                         "link": "http://wordpress.local/books/vengeance-of-the-hunter/"}
    submenu_victory = {"XPath": "//*[@id='menu-primary']/li[3]/ul/li[5]/a", "text": "Victory of the Hawk",
                       "link": "http://wordpress.local/books/victory-of-the-hawk/"}
    submenu_short = {"XPath": "//*[@id='menu-primary']/li[3]/ul/li[6]/a", "text": "Short Stories",
                     "link": "http://wordpress.local/books/short-stories/"}

    # Secondary menu items for the Store menu
    submenu_store = {"XPath": "//*[@id='menu-primary']/li[6]/ul/li/a",
                     "text": "Bone Walker: The Free Court of Seattle Soundtrack",
                     "link": "http://wordpress.local/bone-walker-the-free-court-of-seattle-soundtrack/"}

    def __init__(self, driver):
        """
        Init method for the class
        :param driver: Webdriver object to use
        """
        self.driver = driver
        self.ac = ActionChains(self.driver)

    @property
    def menu_element(self):
        """
        :return: The Webdriver element pointing at the main menu
        """
        return self.driver.find_element(By.ID, self.menu_id)

    @property
    def home_menu_element(self):
        """
        :return: The Webdriver element pointing at the Home menu item
        """
        return self.driver.find_element(By.XPATH, self.menu_home['XPath'])

    @property
    def home_menu_text(self):
        """
        :return: The text of the Home menu item
        """
        return self.home_menu_element.text

    @property
    def home_menu_link(self):
        """
        :return: The Home menu item link
        """
        return self.home_menu_element.get_attribute('href')

    @property
    def home_submenu_element(self):
        """
        :return: The Webdriver element pointing at the submenu under Home
        """
        return self.driver.find_element(By.XPATH, self.submenu_home['XPath'])

    @property
    def home_submenu_text(self):
        """
        :return: The text of the Home submenu item
        """
        return self.home_submenu_element.text

    @property
    def home_submenu_link(self):
        """
        :return: The Home submenu item link
        """
        return self.home_submenu_element.get_attribute('href')

    @property
    def about_menu_element(self):
        """
        :return: The Webdriver element pointing at the About menu item
        """
        return self.driver.find_element(By.XPATH, self.menu_about['XPath'])

    @property
    def about_menu_text(self):
        """
        :return: The text of the About menu item
        """
        return self.about_menu_element.text

    @property
    def about_menu_link(self):
        """
        :return: The About menu item link
        """
        return self.about_menu_element.get_attribute('href')

    @property
    def books_menu_element(self):
        """
        :return: The Webdriver element pointing at the Books menu item
        """
        return self.driver.find_element(By.XPATH, self.menu_books['XPath'])

    @property
    def books_menu_text(self):
        """
        :return: The text of the Books menu item
        """
        return self.books_menu_element.text

    @property
    def books_menu_link(self):
        """
        :return: The Books menu item link
        """
        return self.books_menu_element.get_attribute('href')

    @property
    def books_submenu_element(self):
        """
        :return: The Webdriver element pointing at the submenu under Books
        """
        return self.driver.find_element(By.XPATH, self.submenu_books_xpath)

    @property
    def faerie_submenu_element(self):
        """
        :return: The Webdriver element pointing to the Faerie Blood item under Books
        """
        return self.driver.find_element(By.XPATH, self.submenu_faerie['XPath'])

    @property
    def faerie_submenu_text(self):
        """
        :return: The text of the Faerie Blood submenu item
        """
        return self.faerie_submenu_element.text

    @property
    def faerie_submenu_link(self):
        """
        :return: The link of the Faerie Blood submenu item
        """
        return self.faerie_submenu_element.get_attribute('href')

    @property
    def bone_submenu_element(self):
        """
        :return: The Webdriver element pointing to the Bone Walker item under Books
        """
        return self.driver.find_element(By.XPATH, self.submenu_bone['XPath'])

    @property
    def bone_submenu_text(self):
        """
        :return: The text of the Bone Walker submenu item
        """
        return self.bone_submenu_element.text

    @property
    def bone_submenu_link(self):
        """
        :return: The link of the Bone Walker submenu item
        """
        return self.bone_submenu_element.get_attribute('href')

    @property
    def valor_submenu_element(self):
        """
        :return: The Webdriver element pointing to the Valor of the Healer item under Books
        """
        return self.driver.find_element(By.XPATH, self.submenu_valor['XPath'])

    @property
    def valor_submenu_text(self):
        """
        :return: The text of the Valor of the Healer submenu item
        """
        return self.valor_submenu_element.text

    @property
    def valor_submenu_link(self):
        """
        :return: The link of the Valor of the Healer submenu item
        """
        return self.valor_submenu_element.get_attribute('href')

    @property
    def vengeance_submenu_element(self):
        """
        :return: The Webdriver element pointing to the Vengeance of the Hunter item under Books
        """
        return self.driver.find_element(By.XPATH, self.submenu_vengeance['XPath'])

    @property
    def vengeance_submenu_text(self):
        """
        :return: The text of the Vengeance of the Hunter submenu item
        """
        return self.vengeance_submenu_element.text

    @property
    def vengeance_submenu_link(self):
        """
        :return: The link of the Vengeance of the Hunter submenu item
        """
        return self.vengeance_submenu_element.get_attribute('href')

    @property
    def victory_submenu_element(self):
        """
        :return: The Webdriver element pointing to the Victory of the Hawk item under Books
        """
        return self.driver.find_element(By.XPATH, self.submenu_victory['XPath'])

    @property
    def victory_submenu_text(self):
        """
        :return: The text of the Victory of the Hawk submenu item
        """
        return self.victory_submenu_element.text

    @property
    def victory_submenu_link(self):
        """
        :return: The link of the Victory of the Hawk submenu item
        """
        return self.victory_submenu_element.get_attribute('href')

    @property
    def short_submenu_element(self):
        """
        :return: The Webdriver element pointing to the Short Stories item under Books
        """
        return self.driver.find_element(By.XPATH, self.submenu_short['XPath'])

    @property
    def short_submenu_text(self):
        """
        :return: The text of the Short Stories submenu item
        """
        return self.short_submenu_element.text

    @property
    def short_submenu_link(self):
        """
        :return: The link of the Short Stories submenu item
        """
        return self.short_submenu_element.get_attribute('href')

    @property
    def blog_menu_element(self):
        """
        :return: The Webdriver element pointing at the Blog menu item
        """
        return self.driver.find_element(By.XPATH, self.menu_blog['XPath'])

    @property
    def blog_menu_text(self):
        """
        :return: The text of the Blog menu item
        """
        return self.blog_menu_element.text

    @property
    def blog_menu_link(self):
        """
        :return: The Blog menu item link
        """
        return self.blog_menu_element.get_attribute('href')

    @property
    def contact_menu_element(self):
        """
        :return: The Webdriver element pointing at the Contact menu item
        """
        return self.driver.find_element(By.XPATH, self.menu_contact['XPath'])

    @property
    def contact_menu_text(self):
        """
        :return: The text of the Contact menu item
        """
        return self.contact_menu_element.text

    @property
    def contact_menu_link(self):
        """
        :return: The Contact menu item link
        """
        return self.contact_menu_element.get_attribute('href')

    @property
    def store_menu_element(self):
        """
        :return: The Webdriver element pointing at the Store menu item
        """
        return self.driver.find_element(By.XPATH, self.menu_store['XPath'])

    @property
    def store_menu_text(self):
        """
        :return: The text of the Store menu item
        """
        return self.store_menu_element.text

    @property
    def store_menu_link(self):
        """
        :return: The Store menu item link
        """
        return self.store_menu_element.get_attribute('href')

    @property
    def store_submenu_element(self):
        """
        :return: The Webdriver element pointing at the submenu under Store
        """
        return self.driver.find_element(By.XPATH, self.submenu_store['XPath'])

    @property
    def store_submenu_text(self):
        """
        :return: The text of the Store submenu item
        """
        return self.store_submenu_element.text

    @property
    def store_submenu_link(self):
        """
        :return: The Store submenu item link
        """
        return self.store_submenu_element.get_attribute('href')

    def verify_home_menu(self):
        """
        Verify the Home menu is present, visible, and has the correct text and destination
        """
        assert self.home_menu_element is not None
        assert self.home_menu_element.is_displayed()
        assert self.home_menu_text == self.menu_home['text'], "Home menu does not have correct text."
        assert self.home_menu_link == self.menu_home['link'], "Home menu does not have correct link."
        self.home_menu_element.click()
        assert self.driver.current_url == self.home_menu_link, \
            "Clicking on Home does not go to correct destination."

    def verify_about_menu(self):
        """
        Verify the About menu is present, visible, and has the correct text and destination
        """
        assert self.about_menu_element is not None
        assert self.about_menu_element.is_displayed()
        assert self.about_menu_text == self.menu_about['text'], "About menu does not have correct text."
        assert self.about_menu_link == self.menu_about['link'], "About menu does not have correct link."
        self.about_menu_element.click()
        assert self.driver.current_url == self.about_menu_link, \
            "Clicking on About does not go to correct destination."

    def verify_books_menu(self):
        """
        Verify the Books menu is present, visible, and has the correct text and destination
        """
        assert self.books_menu_element is not None
        assert self.books_menu_element.is_displayed()
        assert self.books_menu_text == self.menu_books['text'], "Books menu does not have correct text."
        assert self.books_menu_link == self.menu_books['link'], "Books menu does not have correct link."
        self.books_menu_element.click()
        assert self.driver.current_url == self.books_menu_link, \
            "Clicking on Books does not go to correct destination."

    def verify_blog_menu(self):
        """
        Verify the Blog menu is present, visible, and has the correct text and destination
        """
        assert self.blog_menu_element is not None
        assert self.blog_menu_element.is_displayed()
        assert self.blog_menu_text == self.menu_blog['text'], "Blog menu does not have correct text."
        assert self.blog_menu_link == self.menu_blog['link'], "Blog menu does not have correct link."
        self.blog_menu_element.click()
        assert self.driver.current_url == self.blog_menu_link, \
            "Clicking on Blog does not go to correct destination."

    def verify_contact_menu(self):
        """
        Verify the Contact menu is present, visible, and has the correct text and destination
        """
        assert self.contact_menu_element is not None
        assert self.contact_menu_element.is_displayed()
        assert self.contact_menu_text == self.menu_contact['text'], \
            "Contact menu does not have correct text."
        assert self.contact_menu_link == self.menu_contact['link'], \
            "Contact menu does not have correct link."
        self.contact_menu_element.click()
        assert self.driver.current_url == self.contact_menu_link, \
            "Clicking on Contact does not go to correct destination."

    def verify_store_menu(self):
        """
        Verify the Store menu is present, visible, and has the correct text and destination
        """
        assert self.store_menu_element is not None
        assert self.store_menu_element.is_displayed()
        assert self.store_menu_text == self.menu_store['text'], "Store menu does not have correct text."
        assert self.store_menu_link == self.menu_store['link'], "Store menu does not have correct link."
        self.store_menu_element.click()
        assert self.driver.current_url == self.menu_store['link'], "Clicking on Store does not go to correct destination."

    def verify_home_submenu(self):
        """
        Verify all aspects of the Home submenu
        """
        # Verify that the Home submenu isn't visible by default
        assert self.home_submenu_element is not None
        assert self.home_submenu_element.is_displayed() is False

        # Verify that the Home submenu becomes visible when you hover over Home
        self.ac.move_to_element(self.home_menu_element).perform()
        assert self.home_submenu_element.is_displayed()
        assert self.home_submenu_text == self.submenu_home['text']
        self.home_submenu_element.click()
        assert self.driver.current_url == self.submenu_home['link']

    def verify_books_submenu(self):
        """
        Verify all aspects of the Books submenu
        """
        # Verify that the Books submenu isn't visible by default
        assert self.books_submenu_element is not None
        assert self.books_submenu_element.is_displayed() is False

        # Verify that the Books submenu becomes visible when you hover over Books
        self.ac.move_to_element(self.books_menu_element).perform()
        assert self.books_submenu_element.is_displayed()

    def verify_faerie_submenu(self):
        """
        Verify the Faerie Blood item on the Books submenu
        """
        self.ac.move_to_element(self.books_menu_element).perform()
        assert self.faerie_submenu_text == self.submenu_faerie['text']
        assert self.faerie_submenu_link == self.submenu_faerie['link']
        self.faerie_submenu_element.click()
        assert self.driver.current_url == self.submenu_faerie['link']

    def verify_bone_submenu(self):
        """
        Verify the Bone Walker item on the Books submenu
        """
        self.ac.move_to_element(self.books_menu_element).perform()
        assert self.bone_submenu_text == self.submenu_bone['text']
        assert self.bone_submenu_link == self.submenu_bone['link']
        self.bone_submenu_element.click()
        assert self.driver.current_url == self.submenu_bone['link']

    def verify_valor_submenu(self):
        """
        Verify the Valor of the Healer item on the Books submenu
        """
        self.ac.move_to_element(self.books_menu_element).perform()
        assert self.valor_submenu_text == self.submenu_valor['text']
        assert self.valor_submenu_link == self.submenu_valor['link']
        self.valor_submenu_element.click()
        assert self.driver.current_url == self.submenu_valor['link']

    def verify_vengeance_submenu(self):
        """
        Verify the Vengeance of the Hunter item on the Books submenu
        """
        self.ac.move_to_element(self.books_menu_element).perform()
        assert self.vengeance_submenu_text == self.submenu_vengeance['text']
        assert self.vengeance_submenu_link == self.submenu_vengeance['link']
        self.vengeance_submenu_element.click()
        assert self.driver.current_url == self.submenu_vengeance['link']

    def verify_victory_submenu(self):
        """
        Verify the Victory of the Hawk item on the Books submenu
        """
        self.ac.move_to_element(self.books_menu_element).perform()
        assert self.victory_submenu_text == self.submenu_victory['text']
        assert self.victory_submenu_link == self.submenu_victory['link']
        self.victory_submenu_element.click()
        assert self.driver.current_url == self.submenu_victory['link']

    def verify_short_submenu(self):
        """
        Verify the Short Stories item on the Books submenu
        """
        self.ac.move_to_element(self.books_menu_element).perform()
        assert self.short_submenu_text == self.submenu_short['text']
        assert self.short_submenu_link == self.submenu_short['link']
        self.short_submenu_element.click()
        assert self.driver.current_url == self.submenu_short['link']

    def verify_store_submenu(self):
        """
        Verify the Store submenu
        """
        assert self.store_submenu_element is not None
        assert self.store_submenu_element.is_displayed() is False
        self.ac.move_to_element(self.store_menu_element).perform()
        assert self.store_submenu_element.is_displayed()
        assert self.store_submenu_text == self.submenu_store['text']
        assert self.store_submenu_link == self.submenu_store['link']
        self.store_submenu_element.click()
        assert self.driver.current_url == self.submenu_store['link']
