import WPMenu
import WPSidebar
import WPFooter

# WPHomepage
# Written by Angela Korra'ti
# Last updated 2/21/2019
#
# This is a helper class to define the layout of the homepage of the test site.


class WPHomepage:
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

    @property
    def site_title_element(self):
        """
        :return: The Webdriver element that refers to the site title.
        """
        return self.driver.find_element_by_class_name(self.wp_lib.site_title['class'])

    @property
    def site_title(self):
        """
        :return: The text of the site title.
        """
        site_title_element = self.driver.find_element_by_class_name(self.wp_lib.site_title['class'])
        return site_title_element.text

    @property
    def site_description_element(self):
        """
        :return: The Webdriver element that refers to the site description.
        """
        return self.driver.find_element_by_class_name(self.wp_lib.site_description['class'])

    @property
    def site_description(self):
        """
        :return: The text of the site description.
        """
        site_description_element = self.driver.find_element_by_class_name(self.wp_lib.site_description['class'])
        return site_description_element.text

    @property
    def primary_menu_element(self):
        """
        :return: The Webdriver element that refers to the primary menu.
        """
        return self.driver.find_element_by_id(self.wp_lib.menu_id)

    @property
    def content_area_element(self):
        """
        :return: The Webdriver element that refers to the overall content area.
        """
        return self.driver.find_element_by_id(self.wp_lib.content_id)

    @property
    def primary_content_area_element(self):
        """
        :return: The Webdriver element that refers to the primary content area.
        """
        return self.driver.find_element_by_id(self.wp_lib.primary_content_id)

    @property
    def secondary_content_area_element(self):
        """
        :return: The Webdriver element that refers to the secondary content area.
        """
        return self.driver.find_element_by_id(self.wp_lib.secondary_content_id)