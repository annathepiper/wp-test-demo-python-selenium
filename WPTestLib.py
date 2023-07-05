# WPTestLib
# Written by Angela Korra'ti
# Last updated 5/10/2019
#
# This is a helper class to contain various test strings, ids, classes, and xpaths.


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
    wp_base_uri = "%s://%s"
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

    # Strings pertaining to the footer.
    footer_id = "colophon"
    footer_social_menu_id = "menu-social-1"
    footer_site_info_class = "site-info"
    footer_site_title_xpath = "//span[@class='site-title']/a"
    footer_wp_link = {"XPath": "//div[@class='site-info']/a", "text": "Proudly powered by WordPress",
                      "link": "https://wordpress.org/"}
    footer_social_facebook = {"XPath": "//ul[@id='menu-social-1']/li[1]/a", "text": "Facebook",
                              "link": "https://www.facebook.com/annathepiper"}
    footer_social_mastodon = {"XPath": "//ul[@id='menu-social-1']/li[2]/a", "text": "Mastodon",
                             "link": "https://mastodon.murkworks.net/@annathepiper"}
    footer_social_github = {"XPath": "//ul[@id='menu-social-1']/li[3]/a", "text": "GitHub",
                          "link": "https://github.com/annathepiper"}
    footer_social_linkedin = {"XPath": "//ul[@id='menu-social-1']/li[4]/a", "text": "LinkedIn",
                            "link": "https://www.linkedin.com/in/angela-korrati"}

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

    # Strings pertaining to the sidebar
    sidebar_search_id = "search-2"
    sidebar_search_input_xpath = "//*[@id='search-2']/form/label/input"
    sidebar_search_input_text = "Search \u2026"
    sidebar_search_button_xpath = "//*[@id='search-2']/form/button"
    sidebar_recent_posts_id = "recent-posts-2"
    sidebar_recent_posts_title_xpath = "//*[@id='recent-posts-2']/h2"
    sidebar_recent_posts_title_text = "RECENT POSTS"
    sidebar_recent_posts_list_xpath = "//*[@id='recent-posts-2']/*/ul"
    sidebar_recent_comments_id = "recent-comments-2"
    sidebar_recent_comments_title_xpath = "//*[@id='recent-comments-2']/h2"
    sidebar_recent_comments_title_text = "RECENT COMMENTS"
    sidebar_recent_comments_list_xpath = "//*[@id='recent-comments-2']/*/ul"
    sidebar_archives_id = "archives-2"
    sidebar_archives_title_xpath = "//*[@id='archives-2']/h2"
    sidebar_archives_title_text = "ARCHIVES"
    sidebar_archives_list_xpath = "//*[@id='archives-2']/*/ul"
    sidebar_categories_id = "categories-2"
    sidebar_categories_title_xpath = "//*[@id='categories-2']/h2"
    sidebar_categories_title_text = "CATEGORIES"
    sidebar_categories_list_xpath = "//*[@id='categories-2']/*/ul"
    sidebar_meta_id = "meta-2"
    sidebar_meta_title_xpath = "//*[@id='meta-2']/h2"
    sidebar_meta_title_text = "META"
    sidebar_meta_list_xpath = "//*[@id='meta-2']/*/ul"

    # Strings pertaining to search
    search_string = "Faerie Blood"
    search_uri = "/?s=Faerie+Blood"
    search_results_string = "Search Results for: "
    search_no_results_string = "Walk the Wards"
    search_no_results_uri = "/?s=Walk+the+Wards"
    search_no_results_message = "Nothing Found"

    # Strings pertaining to testing clicking on Recent Posts
    recent_posts_uri = "/2017/04/17/angelahighland-info-domain-now-active/"
    recent_posts_title = "angelahighland.info domain now active"

    # Strings pertaining to testing clicking on Recent Comments
    recent_comments_uri = "/2016/09/12/hello-readers/#comment-3"
    recent_comments_title = "Hello, readers!"

    # Strings pertaining to testing clicking on Archives
    archives_uri = "/2017/04/"
    archives_string = "Month: "
    archives_title = "April 2017"

    # Strings pertaining to testing clicking on Categories
    categories_uri = "/category/about-me/"
    categories_string = "Category: "
    categories_title = "About Me"

    # Strings pertaining to testing clicking on Meta links
    meta_login_uri = "/wp-login.php"
