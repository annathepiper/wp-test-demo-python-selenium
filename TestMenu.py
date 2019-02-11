from BaseTest import BaseTest
import WPHomepage

# TestMenu
# Written by Angela Korra'ti
# Last updated 2/11/2019
#
# This class conducts tests against the main menu of my test Wordpress site.


class TestMenu(BaseTest):
    wp_homepage = None
    wp_menu = None

    def setUp(self):
        """
        Do setup for the test cases.
        """
        super().setUp()
        self.driver.get(self.wp_lib.wp_base_uri)
        self.wp_homepage = WPHomepage.WPHomepage(self.driver, self.wp_lib)
        self.wp_menu = self.wp_homepage.wp_menu

    def TestMenuExistsVisible(self):
        """
        Verify that the main menu is present and visible
        """
        menu_element = self.wp_menu.menu_element
        assert menu_element is not None
        assert menu_element.is_displayed()

    def TestHomeMenuExistsVisible(self):
        """
        Verify that the Home menu is present and visible        
        """
        home_menu_element = self.wp_menu.home_menu_element
        assert home_menu_element is not None
        assert home_menu_element.is_displayed()

    def TestHomeMenuText(self):
        """
        Verify the Home menu text is correct
        """
        assert self.wp_menu.home_menu_text == self.wp_lib.menu_home['text']

    def TestHomeMenuLink(self):
        """
        Verify the Home menu link is correct
        """
        assert self.wp_menu.home_menu_link == self.wp_lib.menu_home['link']

    def TestHomeMenuLinkClick(self):
        """
        Verify clicking the Home menu link lands you on the homepage        
        """
        self.wp_menu.home_menu_element.click()
        assert self.driver.current_url == self.wp_menu.home_menu_link

    def TestAboutMenuExistsVisible(self):
        """
        Verify that the About menu is present and visible
        """
        about_menu_element = self.wp_menu.about_menu_element
        assert about_menu_element is not None
        assert about_menu_element.is_displayed()

    def TestAboutMenuText(self):
        """
        Verify the About menu text is correct
        """
        assert self.wp_menu.about_menu_text == self.wp_lib.menu_about['text']

    def TestAboutMenuLink(self):
        """
        Verify the About menu link is correct
        """
        assert self.wp_menu.about_menu_link == self.wp_lib.menu_about['link']

    def TestAboutMenuLinkClick(self):
        """
        Verify clicking the About menu link lands you on the About page
        """
        self.wp_menu.about_menu_element.click()
        assert self.driver.current_url == self.wp_menu.about_menu_link

    def TestBooksMenuExistsVisible(self):
        """
        Verify that the Books menu is present and visible
        """
        books_menu_element = self.wp_menu.books_menu_element
        assert books_menu_element is not None
        assert books_menu_element.is_displayed()

    def TestBooksMenuText(self):
        """
        Verify the Books menu text is correct
        """
        assert self.wp_menu.books_menu_text == self.wp_lib.menu_books['text']

    def TestBooksMenuLink(self):
        """
        Verify the Books menu link is correct
        """
        assert self.wp_menu.books_menu_link == self.wp_lib.menu_books['link']

    def TestBooksMenuLinkClick(self):
        """
        Verify clicking the Books menu link lands you on the Books page
        """
        self.wp_menu.books_menu_element.click()
        assert self.driver.current_url == self.wp_menu.books_menu_link

    def TestBlogMenuExistsVisible(self):
        """
        Verify that the Blog menu is present and visible
        """
        blog_menu_element = self.wp_menu.blog_menu_element
        assert blog_menu_element is not None
        assert blog_menu_element.is_displayed()

    def TestBlogMenuText(self):
        """
        Verify the Blog menu text is correct
        """
        assert self.wp_menu.blog_menu_text == self.wp_lib.menu_blog['text']

    def TestBlogMenuLink(self):
        """
        Verify the Blog menu link is correct
        """
        assert self.wp_menu.blog_menu_link == self.wp_lib.menu_blog['link']

    def TestBlogMenuLinkClick(self):
        """
        Verify clicking the Blog menu link lands you on the Blog page
        """
        self.wp_menu.blog_menu_element.click()
        assert self.driver.current_url == self.wp_menu.blog_menu_link
