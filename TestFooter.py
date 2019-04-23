from BaseTest import BaseTest
import WPHomepage
from selenium.webdriver.common.action_chains import ActionChains

# TestFooter
# Written by Angela Korra'ti
# Last updated 3/6/2019
#
# This class conducts tests against the footer on the homepage of my test Wordpress site.


class TestFooter(BaseTest):
    wp_footer = None
    ac = None

    @classmethod
    def setUpClass(self):
        """
        Do setup for the test cases.
        """
        super().setUp()
        self.driver.get(self.wp_lib.wp_base_uri)
        self.wp_footer = WPHomepage.WPHomepage(self.driver, self.wp_lib).wp_footer
        self.ac = ActionChains(self.driver)

    def TestFooterSiteTitle(self):
        """
        Verify the footer site title element is present and visible
        """
        footer_site_title_element = self.wp_footer.footer_site_title_element
        assert footer_site_title_element is not None
        assert footer_site_title_element.is_displayed()

    def TestFooterSiteTitleText(self):
        """
        Verify that the footer site title element has the correct text
        """
        assert self.wp_footer.footer_site_title_text == self.wp_lib.site_title['text']

    def TestFooterSiteTitleLinkClick(self):
        """
        Verify clicking on the footer site title link takes you to the homepage
        """
        self.ac.move_to_element(self.wp_footer.footer_element).perform()
        self.ac.move_to_element(self.wp_footer.footer_site_title_element).perform()
        self.wp_footer.footer_site_title_element.click()
        assert self.driver.current_url == self.wp_lib.menu_home['link']

    def TestFooterWordpress(self):
        """
        Verify the footer Wordpress element is present and visible
        """
        footer_wordpress_element = self.wp_footer.footer_wordpress_element
        assert footer_wordpress_element is not None
        assert footer_wordpress_element.is_displayed()

    def TestFooterWordpressText(self):
        """
        Verify that the footer Wordpress element has the correct text
        """
        # Have to move to the elements to get Selenium to actually find them
        self.ac.move_to_element(self.wp_footer.footer_element).perform()
        self.ac.move_to_element(self.wp_footer.footer_wordpress_element).perform()
        assert self.wp_footer.footer_wordpress_element_text == self.wp_lib.footer_wp_link['text']

    def TestFooterWordpressLinkClick(self):
        """
        Verify that clicking on the footer Wordpress link lands on correct page (wordpress.org)
        """
        # Have to move to the elements to get Selenium to actually find them
        self.ac.move_to_element(self.wp_footer.footer_element).perform()
        self.ac.move_to_element(self.wp_footer.footer_wordpress_element).perform()
        self.wp_footer.footer_wordpress_element.click()
        assert self.driver.current_url == self.wp_lib.footer_wp_link['link']

    def TestFooterSocialFacebook(self):
        """
        Verify the footer Facebook element is present and visible
        """
        footer_facebook_element = self.wp_footer.footer_wordpress_social_facebook_element
        assert footer_facebook_element is not None
        assert footer_facebook_element.is_displayed()

    def TestFooterSocialFacebookText(self):
        """
        Verify that the footer Facebook element has the correct text
        """
        assert self.wp_footer.footer_wordpress_social_facebook_text == self.wp_lib.footer_social_facebook['text']

    def TestFooterSocialFacebookLinkClick(self):
        """
        Verify that clicking the footer Facebook link lands on correct page
        """
        self.ac.move_to_element(self.wp_footer.footer_element).perform()
        self.ac.move_to_element(self.wp_footer.footer_wordpress_element).perform()
        self.wp_footer.footer_wordpress_social_facebook_element.click()
        assert self.driver.current_url == self.wp_lib.footer_social_facebook['link']

    def TestFooterSocialTwitter(self):
        """
        Verify the footer Twitter element is present and visible
        """
        footer_twitter_element = self.wp_footer.footer_wordpress_social_twitter_element
        assert footer_twitter_element is not None
        assert footer_twitter_element.is_displayed()

    def TestFooterSocialTwitterText(self):
        """
        Verify that the footer Twitter element has the correct text
        """
        assert self.wp_footer.footer_wordpress_social_twitter_text == self.wp_lib.footer_social_twitter['text']

    def TestFooterSocialTwitterLinkClick(self):
        """
        Verify that clicking the footer Twitter link lands on correct page
        """
        self.ac.move_to_element(self.wp_footer.footer_element).perform()
        self.ac.move_to_element(self.wp_footer.footer_wordpress_element).perform()
        self.wp_footer.footer_wordpress_social_twitter_element.click()
        assert self.driver.current_url == self.wp_lib.footer_social_twitter['link']

    def TestFooterSocialGithub(self):
        """
        Verify the footer Github element is present and visible
        """
        footer_github_element = self.wp_footer.footer_wordpress_social_github_element
        assert footer_github_element is not None
        assert footer_github_element.is_displayed()

    def TestFooterSocialGithubText(self):
        """
        Verify that the footer Github element has the correct text
        """
        assert self.wp_footer.footer_wordpress_social_github_text == self.wp_lib.footer_social_github['text']

    def TestFooterSocialGithubLinkClick(self):
        """
        Verify that clicking the footer Github link lands on correct page
        """
        self.ac.move_to_element(self.wp_footer.footer_element).perform()
        self.ac.move_to_element(self.wp_footer.footer_wordpress_element).perform()
        self.wp_footer.footer_wordpress_social_github_element.click()
        assert self.driver.current_url == self.wp_lib.footer_social_github['link']

    def TestFooterSocialLinkedIn(self):
        """
        Verify the footer LinkedIn element is present and visible
        """
        footer_linkedin_element = self.wp_footer.footer_wordpress_social_linkedin_element
        assert footer_linkedin_element is not None
        assert footer_linkedin_element.is_displayed()

    def TestFooterSocialLinkedInText(self):
        """
        Verify that the footer LinkedIn element has the correct text
        """
        assert self.wp_footer.footer_wordpress_social_linkedin_text == self.wp_lib.footer_social_linkedin['text']

    def TestFooterSocialLinkedInLinkClick(self):
        """
        Verify that clicking the footer LinkedIn link lands on correct page
        """
        self.ac.move_to_element(self.wp_footer.footer_element).perform()
        self.ac.move_to_element(self.wp_footer.footer_wordpress_element).perform()
        self.wp_footer.footer_wordpress_social_linkedin_element.click()
        assert self.driver.current_url.startswith("https://www.linkedin.com")
