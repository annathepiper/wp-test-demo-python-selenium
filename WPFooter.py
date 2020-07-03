# WPFooter
# Written by Angela Korra'ti
# Last updated 4/24/2019
#
# This is a helper class to define the layout of the footer. Used in turn by page level classes.


class WPFooter:
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
    def footer_element(self):
        """
        :return: The Webdriver element that refers to the footer
        """
        return self.driver.find_element_by_id(self.wp_lib.footer_id)

    @property
    def social_menu_element(self):
        """
        :return: The Webdriver element that refers to the footer social menu
        """
        return self.driver.find_element_by_id(self.wp_lib.footer_social_menu_id)

    @property
    def site_info_element(self):
        """
        :return: The Webdriver element that refers to the footer site info section
        """
        return self.driver.find_element_by_class_name(self.wp_lib.footer_site_info_class)

    @property
    def site_title_element(self):
        """
        :return: The Webdriver element that refers to the footer site title section
        """
        return self.driver.find_element_by_xpath(self.wp_lib.footer_site_title_xpath)

    @property
    def site_title_text(self):
        """
        :return: The text of the footer site title element
        """
        return self.site_title_element.text

    @property
    def wordpress_element(self):
        """
        :return: The Webdriver element that refers to the footer Wordpress link
        """
        return self.driver.find_element_by_xpath(self.wp_lib.footer_wp_link['XPath'])

    @property
    def wordpress_element_text(self):
        """
        :return: The text of the footer Wordpress link
        """
        return self.wordpress_element.text

    @property
    def social_facebook_element(self):
        """
        :return: The Webdriver element that refers to the Facebook link in the social section of the footer
        """
        return self.driver.find_element_by_xpath(self.wp_lib.footer_social_facebook['XPath'])

    @property
    def social_facebook_text(self):
        """
        :return: The text of the footer social Facebook link
        """
        return self.social_facebook_element.text

    @property
    def social_twitter_element(self):
        """
        :return: The Webdriver element that refers to the Twitter link in the social section of the footer
        """
        return self.driver.find_element_by_xpath(self.wp_lib.footer_social_twitter['XPath'])

    @property
    def social_twitter_text(self):
        """
        :return: The text of the footer social Twitter link
        """
        return self.social_twitter_element.text

    @property
    def social_github_element(self):
        """
        :return: The Webdriver element that refers to the Github link in the social section of the footer
        """
        return self.driver.find_element_by_xpath(self.wp_lib.footer_social_github['XPath'])

    @property
    def social_github_text(self):
        """
        :return: The text of the footer social Github link
        """
        return self.social_github_element.text

    @property
    def social_linkedin_element(self):
        """
        :return: The Webdriver element that refers to the LinkedIn link in the social section of the footer
        """
        return self.driver.find_element_by_xpath(self.wp_lib.footer_social_linkedin['XPath'])

    @property
    def social_linkedin_text(self):
        """
        :return: The text of the footer social LinkedIn link
        """
        return self.social_linkedin_element.text
