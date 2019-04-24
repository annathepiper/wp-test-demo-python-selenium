import WPMenu
import WPSidebar
import WPFooter

# WPHomepage
# Written by Angela Korra'ti
# Last updated 4/24/2019
#
# This is a helper class to define the layout of a post on the test site.


class WPPost:
    driver = None
    wp_lib = None
    wp_menu = None
    wp_sidebar = None
    wp_footer = None

    def __init__(self, driver, wp_lib):
        """
        Init method.
        :param driver: Webdriver object
        :param wp_lib: wp_lib object for the helper class to get ids, classes, xpaths
        """
        self.driver = driver
        self.wp_lib = wp_lib

        # Initialize the menu object
        self.wp_menu = WPMenu.WPMenu(self.driver, self.wp_lib)

        # Initialize the sidebar object
        self.wp_sidebar = WPSidebar.WPSidebar(self.driver, self.wp_lib)

        # Initialize the footer object
        self.wp_footer = WPFooter.WPFooter(self.driver, self.wp_lib)

