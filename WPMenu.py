# WPMenu
# Written by Angela Korra'ti
# Last updated 2/11/2019
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
        return self.driver.find_element_by_id(self.wp_lib.menu_id)

    @property
    def home_menu_element(self):
        """
        :return: The Webdriver element pointing at the Home menu item
        """
        return self.driver.find_element_by_xpath(self.wp_lib.menu_home['XPath'])

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
    def about_menu_element(self):
        """
        :return: The Webdriver element pointing at the About menu item
        """
        return self.driver.find_element_by_xpath(self.wp_lib.menu_about['XPath'])

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
        return self.driver.find_element_by_xpath(self.wp_lib.menu_books['XPath'])

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
    def blog_menu_element(self):
        """
        :return: The Webdriver element pointing at the Blog menu item
        """
        return self.driver.find_element_by_xpath(self.wp_lib.menu_blog['XPath'])

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
        return self.driver.find_element_by_xpath(self.wp_lib.menu_contact['XPath'])

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
