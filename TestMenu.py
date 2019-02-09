from BaseTest import BaseTest
import WPHomepage

# TestMenu
# Written by Angela Korra'ti
# Last updated 2/8/2019
#
# This class conducts tests against the main menu of my test Wordpress site.

class TestMenu(BaseTest):
    wpHomepage = None
    wpMenu = None

    def setUp(self):
        '''Do setup for the test cases.'''
        super().setUp()
        self.driver.get(self.wpLib.wpBaseUri)
        self.wpHomepage = WPHomepage.WPHomepage(self.driver, self.wpLib)
        self.wpMenu = self.wpHomepage.wpMenu

    def TestMenuExistsVisible(self):
        '''
        Verify that the main menu is present and visible
        '''
        menuElement = self.wpMenu.menuElement()
        assert menuElement is not None
        assert menuElement.is_displayed()

    def TestHomeMenuExistsVisible(self):
        '''
        Verify that the Home menu is present and visible
        '''
        homeMenuElement = self.wpMenu.homeMenuElement()
        assert homeMenuElement is not None
        assert homeMenuElement.is_displayed()

    def TestHomeMenuText(self):
        '''
        Verify the Home menu text is correct
        '''
        assert self.wpMenu.homeMenuText == self.wpLib.menuHome['text']

    def TestHomeMenuLink(self):
        '''
        Verify the Home menu link is correct
        '''
        assert self.wpMenu.homeMenuLink == self.wpLib.menuHome['link']

    def TestHomeMenuLinkClick(self):
        '''
        Verify clicking the Home menu link lands you on the homepage
        '''
        self.wpMenu.homeMenuElement().click()
        assert self.driver.current_url == self.wpMenu.homeMenuLink

    def TestAboutMenuExistsVisible(self):
        '''
        Verify that the About menu is present and visible
        '''
        aboutMenuElement = self.wpMenu.aboutMenuElement()
        assert aboutMenuElement is not None
        assert aboutMenuElement.is_displayed()

    def TestAboutMenuText(self):
        '''
        Verify the About menu text is correct
        '''
        assert self.wpMenu.aboutMenuText == self.wpLib.menuAbout['text']

    def TestAboutMenuLink(self):
        '''
        Verify the About menu link is correct
        '''
        assert self.wpMenu.aboutMenuLink == self.wpLib.menuAbout['link']

    def TestAboutMenuLinkClick(self):
        '''
        Verify clicking the About menu link lands you on the About page
        '''
        self.wpMenu.aboutMenuElement().click()
        assert self.driver.current_url == self.wpMenu.aboutMenuLink

    def TestBooksMenuExistsVisible(self):
        '''
        Verify that the Books menu is present and visible
        '''
        booksMenuElement = self.wpMenu.booksMenuElement()
        assert booksMenuElement is not None
        assert booksMenuElement.is_displayed()

    def TestBooksMenuText(self):
        '''
        Verify the Books menu text is correct
        '''
        assert self.wpMenu.booksMenuText == self.wpLib.menuBooks['text']

    def TestBooksMenuLink(self):
        '''
        Verify the Books menu link is correct
        '''
        assert self.wpMenu.booksMenuLink == self.wpLib.menuBooks['link']

    def TestBooksMenuLinkClick(self):
        '''
        Verify clicking the Books menu link lands you on the Books page
        '''
        self.wpMenu.booksMenuElement().click()
        assert self.driver.current_url == self.wpMenu.booksMenuLink