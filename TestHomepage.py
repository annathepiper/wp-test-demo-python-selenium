from BaseTest import BaseTest
import WPHomepage

# TestHomepage
# Written by Angela Korra'ti
# Last updated 2/8/2019
#
# This class conducts tests against the homepage of my test Wordpress site.

class TestHomepage(BaseTest):
    wpHomepage = None

    def setUp(self):
        '''Do setup for the test cases.'''
        super().setUp()
        self.driver.get(self.wpLib.wpBaseUri)
        self.wpHomepage = WPHomepage.WPHomepage(self.driver, self.wpLib)

    def testHomepageTitle(self):
        '''
        Verify that the homepage has the correct title
        '''
        assert self.wpHomepage.siteTitle == self.wpLib.siteTitle['text']
        assert self.wpHomepage.siteTitleElement().is_displayed() is True

    def testHomepageDescription(self):
        '''
        Verify that the homepage has the correct description
        '''
        assert self.wpHomepage.siteDescription == self.wpLib.siteDescription['text']
        assert self.wpHomepage.siteDescriptionElement().is_displayed() is True

    def testPrimaryMenuExistsVisible(self):
        '''
        Verify that the primary menu is present and visible on the homepage
        '''
        menu = self.wpHomepage.primaryMenuElement()
        assert menu is not None
        assert menu.is_displayed()

    def testContentAreaExistsVisible(self):
        '''
        Verify that the overall content area is present and visible on the homepage
        '''
        content = self.wpHomepage.contentAreaElement()
        assert content is not None
        assert content.is_displayed()

    def testPrimaryContentAreaExistsVisible(self):
        '''
        Verify that the primary content area is present and visible on the homepage
        '''
        content = self.wpHomepage.primaryContentAreaElement()
        assert content is not None
        assert content.is_displayed()

    def testSecondaryContentAreaExistsVisible(self):
        '''
        Verify that the secondary content area is present and visible on the homepage
        '''
        content = self.wpHomepage.secondaryContentAreaElement()
        assert content is not None
        assert content.is_displayed()

    def testFooterExistsVisible(self):
        '''
        Verify that the footer is present and visible on the homepage
        '''
        footer = self.wpHomepage.footerElement()
        assert footer is not None
        assert footer.is_displayed()

    def testFooterSocialMenuExistsVisible(self):
        '''
        Verify that the footer social menu is present and visible on the homepage
        '''
        footerSocialMenu = self.wpHomepage.footerSocialMenuElement()
        assert footerSocialMenu is not None
        assert footerSocialMenu.is_displayed()

    def testFooterSiteInfoExistsVisible(self):
        '''
        Verify that the footer site info section is present and visible on the homepage
        '''
        footerSiteInfo = self.wpHomepage.footerSiteInfoElement()
        assert footerSiteInfo is not None
        assert footerSiteInfo.is_displayed()