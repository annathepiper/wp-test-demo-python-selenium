from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


# WPFooter
# Written by Angela Korra'ti
# Last updated 7/19/2023
#
# This is a helper class to define the layout of the footer. Used in turn by page level classes.


class WPFooter:
    driver = None
    wp_lib = None
    ac = None
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

    def __init__(self, driver, wp_lib):
        """
        Init method for the class
        :param driver: Webdriver object to use
        :param wp_lib: Instance of WPTestLib support class for ids, classes, XPaths, etc.
        """
        self.driver = driver
        self.wp_lib = wp_lib
        self.ac = ActionChains(self.driver)

    @property
    def footer_element(self):
        """
        :return: The Webdriver element that refers to the footer
        """
        return self.driver.find_element(By.ID, self.footer_id)

    @property
    def social_menu_element(self):
        """
        :return: The Webdriver element that refers to the footer social menu
        """
        return self.driver.find_element(By.ID, self.footer_social_menu_id)

    @property
    def site_info_element(self):
        """
        :return: The Webdriver element that refers to the footer site info section
        """
        return self.driver.find_element(By.CLASS_NAME, self.footer_site_info_class)

    @property
    def site_title_element(self):
        """
        :return: The Webdriver element that refers to the footer site title section
        """
        return self.driver.find_element(By.XPATH, self.footer_site_title_xpath)

    @property
    def site_title_text(self):
        """
        :return: The text of the footer site title element
        """
        return self.site_title_element.text

    @property
    def wordpress_element(self):
        """
        :return: The Webdriver element that refers to the footer WordPress link
        """
        return self.driver.find_element(By.XPATH, self.footer_wp_link['XPath'])

    @property
    def wordpress_element_text(self):
        """
        :return: The text of the footer WordPress link
        """
        return self.wordpress_element.text

    @property
    def social_facebook_element(self):
        """
        :return: The Webdriver element that refers to the Facebook link in the social section of the footer
        """
        return self.driver.find_element(By.XPATH, self.footer_social_facebook['XPath'])

    @property
    def social_facebook_text(self):
        """
        :return: The text of the footer social Facebook link
        """
        return self.social_facebook_element.text

    @property
    def social_mastodon_element(self):
        """
        :return: The Webdriver element that refers to the Mastodon link in the social section of the footer
        """
        return self.driver.find_element(By.XPATH, self.footer_social_mastodon['XPath'])

    @property
    def social_mastodon_text(self):
        """
        :return: The text of the footer social Mastodon link
        """
        return self.social_mastodon_element.text

    @property
    def social_github_element(self):
        """
        :return: The Webdriver element that refers to the GitHub link in the social section of the footer
        """
        return self.driver.find_element(By.XPATH, self.footer_social_github['XPath'])

    @property
    def social_github_text(self):
        """
        :return: The text of the footer social GitHub link
        """
        return self.social_github_element.text

    @property
    def social_linkedin_element(self):
        """
        :return: The Webdriver element that refers to the LinkedIn link in the social section of the footer
        """
        return self.driver.find_element(By.XPATH, self.footer_social_linkedin['XPath'])

    @property
    def social_linkedin_text(self):
        """
        :return: The text of the footer social LinkedIn link
        """
        return self.social_linkedin_element.text

    def verify_site_title(self):
        """
        Verify that the site title link is present, visible, and has the correct text and destination.
        """
        assert self.site_title_element is not None, "Site title doesn't have the correct text."
        assert self.site_title_element.is_displayed()
        assert self.site_title_text == self.wp_lib.site_title['text']
        self.ac.move_to_element(self.footer_element).perform()
        self.ac.move_to_element(self.site_title_element).perform()
        self.site_title_element.click()
        assert self.driver.current_url == self.wp_lib.wp_base_uri, "Site title link isn't correct."

    def verify_wordpress(self):
        """
        Verify the footer WordPress element is present and visible, and has the correct text and destination.
        """
        assert self.wordpress_element is not None
        assert self.wordpress_element.is_displayed()

        # Have to move to the elements to get Selenium to actually find them
        self.ac.move_to_element(self.footer_element).perform()
        self.ac.move_to_element(self.wordpress_element).perform()
        assert self.wordpress_element_text == self.footer_wp_link['text'], \
            "WordPress footer link doesn't have correct text."
        self.wordpress_element.click()
        assert self.driver.current_url == self.footer_wp_link['link'], \
            "Clicking on Wordpress link doesn't go to expected URL."

    def verify_social_facebook(self):
        """
        Verify the footer Facebook element is present and visible, and has the correct text and destination.
        """
        assert self.social_facebook_element is not None
        assert self.social_facebook_element.is_displayed()
        assert self.social_facebook_text == self.footer_social_facebook['text'], \
            "Facebook link doesn't have correct text."
        self.ac.move_to_element(self.footer_element).perform()
        self.ac.move_to_element(self.social_facebook_element).perform()
        self.social_facebook_element.click()

        # 7/6/2023 Current behavior seems to be that Facebook may sometimes ask for a login
        # and sometimes not. So I'm going to check for both scenarios.
        facebook_wants_login = "https://www.facebook.com/login/?next=https%3A%2F%2Fwww.facebook.com%2Fannathepiper"
        assert self.driver.current_url == facebook_wants_login or \
               self.driver.current_url == self.footer_social_facebook['link'], \
               "Clicking on Facebook link doesn't go to expected destination."

    def verify_social_mastodon(self):
        """
        Verify the footer Mastodon element is present and visible, and has the correct text and destination.
        """
        assert self.social_mastodon_element is not None
        assert self.social_mastodon_element.is_displayed()
        assert self.social_mastodon_text == self.footer_social_mastodon['text'], \
            "Mastodon link doesn't have correct text."
        self.ac.move_to_element(self.footer_element).perform()
        self.ac.move_to_element(self.social_mastodon_element).perform()
        self.social_mastodon_element.click()
        assert self.driver.current_url == self.footer_social_mastodon['link'], \
            "Clicking on Mastodon link doesn't go to correct destination."

    def verify_social_github(self):
        """
        Verify the footer GitHub element is present and visible, and has the correct text and destination.
        """
        assert self.social_github_element is not None
        assert self.social_github_element.is_displayed()
        assert self.social_github_text == self.footer_social_github['text'], \
            "Github link doesn't have correct text."
        self.ac.move_to_element(self.footer_element).perform()
        self.ac.move_to_element(self.social_github_element).perform()
        self.social_github_element.click()
        assert self.driver.current_url == self.footer_social_github['link'], \
            "Clicking on Github link doesn't go to expected destination."

    def verify_social_linkedin(self):
        """
        Verify the footer LinkedIn element is present and visible, and has the correct text and destination.
        """
        assert self.social_linkedin_element is not None
        assert self.social_linkedin_element.is_displayed()
        assert self.social_linkedin_text == self.footer_social_linkedin['text'], \
            "LinkedIn link doesn't have correct text."
        self.ac.move_to_element(self.footer_element).perform()
        self.ac.move_to_element(self.social_linkedin_element).perform()
        self.social_linkedin_element.click()

        # 7/5/2023 Current behavior of LinkedIn link is that sometimes the link has a referer
        # parameter on the end, and sometimes it doesn't, so let's check for both possibilities
        linkedin_referer_suffix = "?original_referer=http%3A%2F%2Fwordpress.local%2F"
        assert (self.driver.current_url == self.footer_social_linkedin['link']) or \
               (self.driver.current_url == self.footer_social_linkedin['link'] +
                linkedin_referer_suffix)
