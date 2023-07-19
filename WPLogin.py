from selenium.webdriver.common.by import By

# WPLogin
# Written by Angela Korra'ti
# Last updated 7/18/2023
#
# This is a helper class to define the layout of the login page of the test site.


class WPLogin:
    driver = None
    wp_lib = None

    def __init__(self, driver, wp_lib):
        """
        Init method.
        :param driver: Webdriver object
        :param wp_lib: wp_lib object for the helper class to get ids, classes, xpaths
        """
        self.driver = driver
        self.wp_lib = wp_lib

    @property
    def username_field(self):
        """
        :return: The Webdriver element that refers to the username field.
        """
        return self.driver.find_element(By.CLASS_NAME, self.wp_lib.login_username_xpath)

    @property
    def password_field(self):
        """
        :return: The Webdriver element that refers to the password field.
        """
        return self.driver.find_element(By.CLASS_NAME, self.wp_lib.login_password_xpath)

    @property
    def login_button(self):
        """
        :return: The Webdriver element that refers to the login button.
        """
        return self.driver.find_element(By.CLASS_NAME, self.wp_lib.login_button_xpath)

    @property
    def back_to_blog(self):
        """
        :return: The Webdriver element that refers to the link to return to the homepage.
        """
        return self.driver.find_element(By.CLASS_NAME, self.wp_lib.back_to_blog_xpath)
