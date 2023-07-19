# WPTestLib
# Written by Angela Korra'ti
# Last updated 7/19/2023
#
# This is a helper class to contain various test strings, ids, classes, and XPaths.


class WPTestLib:
    def __init__(self, protocol=None, host=None):
        if protocol is not None:
            self.protocol = protocol
        if host is not None:
            self.host = host
        self.wp_base_uri = self.wp_base_uri % (self.protocol, self.host)
        self.wp_post_uri = self.wp_base_uri + self.wp_post_uri

    # These values are all top-level things about the site and the Selenium hub
    selenium_host = "http://localhost:4444/wd/hub"
    protocol = "http"
    host = "wordpress.local"
    wp_base_uri = "%s://%s/"
    site_title = {"class": "site-title", "text": "Anna's Dev Wordpress"}
    site_description = {"class": "site-description", "text": "Just another WordPress site"}
    page_title_class = "page-title"
    entry_title_class = "entry-title"

    # Strings for test Uris
    wp_post_uri = "/2016/09/13/testing-testing-testing-is-this-thing-on/"
    post_title = "Testing, testing, testing, is this thing on?"

    # Strings pertaining to the main content areas.
    content_id = "content"
    primary_content_id = "primary"
    secondary_content_id = "secondary"

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
