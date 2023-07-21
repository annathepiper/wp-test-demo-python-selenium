import WPMenu
import WPSidebar
import WPFooter
from selenium.webdriver.common.by import By
import pytest

# WPHomepage
# Written by Angela Korra'ti
# Last updated 7/21/2023
#
# This is a helper class to define the layout of the homepage of the test site.


@pytest.mark.usefixtures("setup_webdriver")
class WPHomepage:
    # driver = None
    wp_lib = None
    wp_menu = None
    wp_sidebar = None
    wp_footer = None

    # def __init__(self, driver, wp_lib):
    def __init__(self, wp_lib):
        """
        Init method.
        :param driver: Webdriver object
        :param wp_lib: wp_lib object for the helper class to get ids, classes, xpaths
        """
        # self.driver = driver
        self.wp_lib = wp_lib

        # Initialize the menu object
        self.wp_menu = WPMenu.WPMenu(self.driver)

        # Initialize the sidebar object
        self.wp_sidebar = WPSidebar.WPSidebar(self.driver, self.wp_lib)

        # Initialize the footer object
        self.wp_footer = WPFooter.WPFooter(self.driver, self.wp_lib)

    @property
    def site_title_element(self):
        """
        :return: The Webdriver element that refers to the site title.
        """
        return self.driver.find_element(By.CLASS_NAME, self.wp_lib.site_title['class'])

    @property
    def site_title(self):
        """
        :return: The text of the site title.
        """
        site_title_element = self.driver.find_element(By.CLASS_NAME, self.wp_lib.site_title['class'])
        return site_title_element.text

    @property
    def site_description_element(self):
        """
        :return: The Webdriver element that refers to the site description.
        """
        return self.driver.find_element(By.CLASS_NAME, self.wp_lib.site_description['class'])

    @property
    def site_description(self):
        """
        :return: The text of the site description.
        """
        site_description_element = self.driver.find_element(By.CLASS_NAME, self.wp_lib.site_description['class'])
        return site_description_element.text

    @property
    def content_area_element(self):
        """
        :return: The Webdriver element that refers to the overall content area.
        """
        return self.driver.find_element(By.ID, self.wp_lib.content_id)

    @property
    def primary_content_area_element(self):
        """
        :return: The Webdriver element that refers to the primary content area.
        """
        return self.driver.find_element(By.ID, self.wp_lib.primary_content_id)

    @property
    def secondary_content_area_element(self):
        """
        :return: The Webdriver element that refers to the secondary content area.
        """
        return self.driver.find_element(By.ID, self.wp_lib.secondary_content_id)