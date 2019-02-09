# WPMenu
# Written by Angela Korra'ti
# Last updated 2/8/2019
#
# This is a helper class to define the layout of the main menu. Used in turn by page level classes.

class WPMenu:
    driver = None
    wpLib = None

    def __init__(self, driver, wpLib):
        '''
        Init method for the class
        :param driver: Webdriver object to use
        :param wpLib: Instance of WPTestLib support class for ids, classes, xpaths, etc.
        '''
        self.driver = driver
        self.wpLib = wpLib

    def menuElement(self):
        '''
        :return: The Webdriver element pointing at the main menu
        '''
        return self.driver.find_element_by_id(self.wpLib.menuId)

    def homeMenuElement(self):
        '''
        :return: The Webdriver element pointing at the Home menu item
        '''
        return self.driver.find_element_by_xpath(self.wpLib.menuHome['XPath'])

    @property
    def homeMenuText(self):
        '''
        :return: The text of the Home menu item
        '''
        return self.homeMenuElement().text

    @property
    def homeMenuLink(self):
        '''
        :return: The Home menu item link
        '''
        return self.homeMenuElement().get_attribute('href')

    def aboutMenuElement(self):
        '''
        :return: The Webdriver element pointing at the About menu item
        '''
        return self.driver.find_element_by_xpath(self.wpLib.menuAbout['XPath'])

    @property
    def aboutMenuText(self):
        '''
        :return: The text of the About menu item
        '''
        return self.aboutMenuElement().text

    @property
    def aboutMenuLink(self):
        '''
        :return: The About menu item link
        '''
        return self.aboutMenuElement().get_attribute('href')

    def booksMenuElement(self):
        '''
        :return: The Webdriver element pointing at the Books menu item
        '''
        return self.driver.find_element_by_xpath(self.wpLib.menuBooks['XPath'])

    @property
    def booksMenuText(self):
        '''
        :return: The text of the Books menu item
        '''
        return self.booksMenuElement().text

    @property
    def booksMenuLink(self):
        '''
        :return: The Books menu item link
        '''
        return self.booksMenuElement().get_attribute('href')