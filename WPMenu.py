from selenium.webdriver.common.by import By

# WPMenu
# Written by Angela Korra'ti
# Last updated 7/7/2023
#
# This is a helper class to define the layout of the main menu. Used in turn by page level classes.


class WPMenu:
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
    def menu_element(self):
        """
        :return: The Webdriver element pointing at the main menu
        """
        return self.driver.find_element(By.ID, self.wp_lib.menu_id)

    @property
    def home_menu_element(self):
        """
        :return: The Webdriver element pointing at the Home menu item
        """
        return self.driver.find_element(By.XPATH, self.wp_lib.menu_home['XPath'])

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
        return self.driver.find_element(By.XPATH, self.wp_lib.submenu_home['XPath'])

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
        return self.driver.find_element(By.XPATH, self.wp_lib.menu_about['XPath'])

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
        return self.driver.find_element(By.XPATH, self.wp_lib.menu_books['XPath'])

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
        return self.driver.find_element(By.XPATH, self.wp_lib.submenu_books_xpath)

    @property
    def faerie_submenu_element(self):
        """
        :return: The Webdriver element pointing to the Faerie Blood item under Books
        """
        return self.driver.find_element(By.XPATH, self.wp_lib.submenu_faerie['XPath'])

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
        return self.driver.find_element(By.XPATH, self.wp_lib.submenu_bone['XPath'])

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
        return self.driver.find_element(By.XPATH, self.wp_lib.submenu_valor['XPath'])

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
        return self.driver.find_element(By.XPATH, self.wp_lib.submenu_vengeance['XPath'])

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
        return self.driver.find_element(By.XPATH, self.wp_lib.submenu_victory['XPath'])

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
        return self.driver.find_element(By.XPATH, self.wp_lib.submenu_short['XPath'])

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
        return self.driver.find_element(By.XPATH, self.wp_lib.menu_blog['XPath'])

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
        return self.driver.find_element(By.XPATH, self.wp_lib.menu_contact['XPath'])

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
        return self.driver.find_element(By.XPATH, self.wp_lib.menu_store['XPath'])

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
        return self.driver.find_element(By.XPATH, self.wp_lib.submenu_store['XPath'])

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
