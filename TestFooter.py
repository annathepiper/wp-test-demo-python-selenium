from BaseTest import BaseTest

# TestFooter
# Written by Angela Korra'ti
# Last updated 4/24/2019
#
# Parent abstract class for testing the footer. Used by child classes that will conduct tests against specific pages.


class TestFooter(BaseTest):
    # HELPER METHODS BEGIN HERE

    def verify_site_title(self, wp_footer):
        """
        Verify the footer site title element is present and visible on the homepage
        """
        site_title_element = wp_footer.site_title_element
        assert site_title_element is not None
        assert site_title_element.is_displayed()

    def verify_site_title_text(self, wp_footer):
        """
        Verify that the footer site title element has the correct text
        """
        assert wp_footer.site_title_text == self.wp_lib.site_title['text']

    def verify_site_title_link_click(self, wp_footer):
        """
        Verify clicking on the footer site title link takes you to the homepage
        """
        self.ac.move_to_element(wp_footer.footer_element).perform()
        self.ac.move_to_element(wp_footer.site_title_element).perform()
        wp_footer.site_title_element.click()
        assert self.driver.current_url == self.wp_lib.menu_home['link']

    def verify_wordpress(self, wp_footer):
        """
        Verify the footer Wordpress element is present and visible
        """
        wordpress_element = wp_footer.wordpress_element
        assert wordpress_element is not None
        assert wordpress_element.is_displayed()

    def verify_wordpress_text(self, wp_footer):
        """
        Verify that the footer Wordpress element has the correct text
        """
        # Have to move to the elements to get Selenium to actually find them
        self.ac.move_to_element(wp_footer.footer_element).perform()
        self.ac.move_to_element(wp_footer.wordpress_element).perform()
        assert wp_footer.wordpress_element_text == self.wp_lib.footer_wp_link['text']

    def verify_wordpress_link_click(self, wp_footer):
        """
        Verify that clicking on the footer Wordpress link lands on correct page (wordpress.org)
        """
        # Have to move to the elements to get Selenium to actually find them
        self.ac.move_to_element(wp_footer.footer_element).perform()
        self.ac.move_to_element(wp_footer.wordpress_element).perform()
        wp_footer.wordpress_element.click()
        assert self.driver.current_url == self.wp_lib.footer_wp_link['link']

    def verify_social_facebook(self, wp_footer):
        """
        Verify the footer Facebook element is present and visible
        """
        facebook_element = wp_footer.social_facebook_element
        assert facebook_element is not None
        assert facebook_element.is_displayed()

    def verify_social_facebook_text(self, wp_footer):
        """
        Verify that the footer Facebook element has the correct text
        """
        assert wp_footer.social_facebook_text == self.wp_lib.footer_social_facebook['text']

    def verify_social_facebook_link_click(self, wp_footer):
        """
        Verify that clicking the footer Facebook link lands on correct page
        """
        self.ac.move_to_element(wp_footer.footer_element).perform()
        self.ac.move_to_element(wp_footer.wordpress_element).perform()
        wp_footer.social_facebook_element.click()
        assert self.driver.current_url == self.wp_lib.footer_social_facebook['link']

    def verify_social_twitter(self, wp_footer):
        """
        Verify the footer Twitter element is present and visible
        """
        twitter_element = wp_footer.social_twitter_element
        assert twitter_element is not None
        assert twitter_element.is_displayed()

    def verify_social_twitter_text(self, wp_footer):
        """
        Verify that the footer Twitter element has the correct text
        """
        assert wp_footer.social_twitter_text == self.wp_lib.footer_social_twitter['text']

    def verify_social_twitter_link_click(self, wp_footer):
        """
        Verify that clicking the footer Twitter link lands on correct page
        """
        self.ac.move_to_element(wp_footer.footer_element).perform()
        self.ac.move_to_element(wp_footer.wordpress_element).perform()
        wp_footer.social_twitter_element.click()
        assert self.driver.current_url == self.wp_lib.footer_social_twitter['link']

    def verify_social_github(self, wp_footer):
        """
        Verify the footer Github element is present and visible
        """
        github_element = wp_footer.social_github_element
        assert github_element is not None
        assert github_element.is_displayed()

    def verify_social_github_text(self, wp_footer):
        """
        Verify that the footer Github element has the correct text
        """
        assert wp_footer.social_github_text == self.wp_lib.footer_social_github['text']

    def verify_social_github_link_click(self, wp_footer):
        """
        Verify that clicking the footer Github link lands on correct page
        """
        self.ac.move_to_element(wp_footer.footer_element).perform()
        self.ac.move_to_element(wp_footer.wordpress_element).perform()
        wp_footer.social_github_element.click()
        assert self.driver.current_url == self.wp_lib.footer_social_github['link']

    def verify_social_linkedin(self, wp_footer):
        """
        Verify the footer LinkedIn element is present and visible
        """
        linkedin_element = wp_footer.social_linkedin_element
        assert linkedin_element is not None
        assert linkedin_element.is_displayed()

    def verify_social_linkedin_text(self, wp_footer):
        """
        Verify that the footer LinkedIn element has the correct text
        """
        assert wp_footer.social_linkedin_text == self.wp_lib.footer_social_linkedin['text']

    def verify_social_linkedin_link_click(self, wp_footer):
        """
        Verify that clicking the footer LinkedIn link lands on correct page
        """
        self.ac.move_to_element(wp_footer.footer_element).perform()
        self.ac.move_to_element(wp_footer.wordpress_element).perform()
        wp_footer.social_linkedin_element.click()
        assert self.driver.current_url.startswith("https://www.linkedin.com")
