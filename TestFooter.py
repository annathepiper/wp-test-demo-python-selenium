from BaseTest import BaseTest

# TestFooter
# Written by Angela Korra'ti
# Last updated 4/26/2019
#
# Parent class for testing the footer. This class conducts tests against the homepage. Child classes will do
# appropriate setup to test other pages.


class TestFooter(BaseTest):
    wp_footer = None

    def set_wp_footer(self, wp_footer):
        """
        Setup function to set the class variable wp_footer used in child tests.
        """
        self.wp_footer = wp_footer

    def verify_site_title(self):
        """
        Verify that the site title link is present, visible, and has the correct text and destination.
        """
        site_title_element = self.wp_footer.site_title_element
        assert site_title_element is not None, "Site title doesn't have the correct text."
        assert site_title_element.is_displayed()
        assert self.wp_footer.site_title_text == self.wp_lib.site_title['text']
        self.ac.move_to_element(self.wp_footer.footer_element).perform()
        self.ac.move_to_element(self.wp_footer.site_title_element).perform()
        self.wp_footer.site_title_element.click()
        assert self.driver.current_url == self.wp_lib.menu_home['link'], "Site title link isn't correct."

    def verify_wordpress(self):
        """
        Verify the footer Wordpress element is present and visible, and has the correct text and destination.
        """
        wordpress_element = self.wp_footer.wordpress_element
        assert wordpress_element is not None
        assert wordpress_element.is_displayed()

        # Have to move to the elements to get Selenium to actually find them
        self.ac.move_to_element(self.wp_footer.footer_element).perform()
        self.ac.move_to_element(self.wp_footer.wordpress_element).perform()
        assert self.wp_footer.wordpress_element_text == self.wp_lib.footer_wp_link['text'],\
            "WordPress footer link doesn't have correct text."
        self.wp_footer.wordpress_element.click()
        assert self.driver.current_url == self.wp_lib.footer_wp_link['link'],\
            "Clicking on Wordpress link doesn't go to expected URL."

    def verify_social_facebook(self):
        """
        Verify the footer Facebook element is present and visible, and has the correct text and destination.
        """
        facebook_element = self.wp_footer.social_facebook_element
        assert facebook_element is not None
        assert facebook_element.is_displayed()
        assert self.wp_footer.social_facebook_text == self.wp_lib.footer_social_facebook['text'],\
            "Facebook link doesn't have correct text."
        self.ac.move_to_element(self.wp_footer.footer_element).perform()
        self.ac.move_to_element(self.wp_footer.social_facebook_element).perform()
        self.wp_footer.social_facebook_element.click()
        assert self.driver.current_url == self.wp_lib.footer_social_facebook['link'],\
            "Clicking on Facebook link doesn't go to expected destination."

    def verify_social_twitter(self):
        """
        Verify the footer Twitter element is present and visible, and has the correct text and destination.
        """
        twitter_element = self.wp_footer.social_twitter_element
        assert twitter_element is not None
        assert twitter_element.is_displayed()
        assert self.wp_footer.social_twitter_text == self.wp_lib.footer_social_twitter['text'],\
            "Twitter link doesn't have correct text."
        self.ac.move_to_element(self.wp_footer.footer_element).perform()
        self.ac.move_to_element(self.wp_footer.social_twitter_element).perform()
        self.wp_footer.social_twitter_element.click()
        assert self.driver.current_url == self.wp_lib.footer_social_twitter['link'],\
            "Clicking on Twitter link doesn't go to correct destination."

    def verify_social_github(self):
        """
        Verify the footer Github element is present and visible, and has the correct text and destination.
        """
        github_element = self.wp_footer.social_github_element
        assert github_element is not None
        assert github_element.is_displayed()
        assert self.wp_footer.social_github_text == self.wp_lib.footer_social_github['text'],\
            "Github link doesn't have correct text."
        self.ac.move_to_element(self.wp_footer.footer_element).perform()
        self.ac.move_to_element(self.wp_footer.social_github_element).perform()
        self.wp_footer.social_github_element.click()
        assert self.driver.current_url == self.wp_lib.footer_social_github['link'],\
            "Clicking on Github link doesn't go to expected destination."

    def verify_social_linkedin(self):
        """
        Verify the footer LinkedIn element is present and visible, and has the correct text and destination.
        """
        linkedin_element = self.wp_footer.social_linkedin_element
        assert linkedin_element is not None
        assert linkedin_element.is_displayed()
        assert self.wp_footer.social_linkedin_text == self.wp_lib.footer_social_linkedin['text'],\
            "LinkedIn link doesn't have correct text."
        self.ac.move_to_element(self.wp_footer.footer_element).perform()
        self.ac.move_to_element(self.wp_footer.social_linkedin_element).perform()
        self.wp_footer.social_linkedin_element.click()
        assert self.driver.current_url.startswith("https://www.linkedin.com")
