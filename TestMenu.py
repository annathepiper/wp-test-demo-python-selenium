from BaseTest import BaseTest

# TestMenu
# Written by Angela Korra'ti
# Last updated 5/10/2019
#
# This class conducts tests against the main menu of my test Wordpress site.


class TestMenu(BaseTest):
    wp_menu = None

    def set_wp_menu(self, wp_menu):
        """
        Setup function to set the class variable wp_menu used in child tests.
        """
        self.wp_menu = wp_menu

    def verify_home_menu(self):
        """
        Verify the Home menu is present, visible, and has the correct text and destination
        """
        home_menu_element = self.wp_menu.home_menu_element
        assert home_menu_element is not None
        assert home_menu_element.is_displayed()
        assert self.wp_menu.home_menu_text == self.wp_lib.menu_home['text'], "Home menu does not have correct text."
        assert self.wp_menu.home_menu_link == self.wp_lib.menu_home['link'], "Home menu does not have correct link."
        self.wp_menu.home_menu_element.click()
        assert self.driver.current_url == self.wp_menu.home_menu_link, \
            "Clicking on Home does not go to correct destination."

    def verify_about_menu(self):
        """
        Verify the About menu is present, visible, and has the correct text and destination
        """
        about_menu_element = self.wp_menu.about_menu_element
        assert about_menu_element is not None
        assert about_menu_element.is_displayed()
        assert self.wp_menu.about_menu_text == self.wp_lib.menu_about['text'], "About menu does not have correct text."
        assert self.wp_menu.about_menu_link == self.wp_lib.menu_about['link'], "About menu does not have correct link."
        self.wp_menu.about_menu_element.click()
        assert self.driver.current_url == self.wp_menu.about_menu_link, \
            "Clicking on About does not go to correct destination."

    def verify_books_menu(self):
        """
        Verify the Books menu is present, visible, and has the correct text and destination
        """
        books_menu_element = self.wp_menu.books_menu_element
        assert books_menu_element is not None
        assert books_menu_element.is_displayed()
        assert self.wp_menu.books_menu_text == self.wp_lib.menu_books['text'], "Books menu does not have correct text."
        assert self.wp_menu.books_menu_link == self.wp_lib.menu_books['link'], "Books menu does not have correct link."
        self.wp_menu.books_menu_element.click()
        assert self.driver.current_url == self.wp_menu.books_menu_link, \
            "Clicking on Books does not go to correct destination."

    def verify_blog_menu(self):
        """
        Verify the Blog menu is present, visible, and has the correct text and destination
        """
        blog_menu_element = self.wp_menu.blog_menu_element
        assert blog_menu_element is not None
        assert blog_menu_element.is_displayed()
        assert self.wp_menu.blog_menu_text == self.wp_lib.menu_blog['text'], "Blog menu does not have correct text."
        assert self.wp_menu.blog_menu_link == self.wp_lib.menu_blog['link'], "Blog menu does not have correct link."
        self.wp_menu.blog_menu_element.click()
        assert self.driver.current_url == self.wp_menu.blog_menu_link, \
            "Clicking on Blog does not go to correct destination."

    def verify_contact_menu(self):
        """
        Verify the Contact menu is present, visible, and has the correct text and destination
        """
        contact_menu_element = self.wp_menu.contact_menu_element
        assert contact_menu_element is not None
        assert contact_menu_element.is_displayed()
        assert self.wp_menu.contact_menu_text == self.wp_lib.menu_contact['text'], \
            "Contact menu does not have correct text."
        assert self.wp_menu.contact_menu_link == self.wp_lib.menu_contact['link'], \
            "Contact menu does not have correct link."
        self.wp_menu.contact_menu_element.click()
        assert self.driver.current_url == self.wp_menu.contact_menu_link, \
            "Clicking on Contact does not go to correct destination."

    def verify_store_menu(self):
        """
        Verify the Store menu is present, visible, and has the correct text and destination
        """
        store_menu_element = self.wp_menu.store_menu_element
        assert store_menu_element is not None
        assert store_menu_element.is_displayed()
        assert self.wp_menu.store_menu_text == self.wp_lib.menu_store['text'], "Store menu does not have correct text."
        assert self.wp_menu.store_menu_link == self.wp_lib.menu_store['link'], "Store menu does not have correct link."
        store_menu_link = self.wp_menu.store_menu_link
        self.wp_menu.store_menu_element.click()
        assert self.driver.current_url == store_menu_link, "Clicking on Store does not go to correct destination."
