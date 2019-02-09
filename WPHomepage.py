import WPMenu

# WPHomepage
# Written by Angela Korra'ti
# Last updated 2/8/2019
#
# This is a helper class to define the layout of the homepage of the test site.

class WPHomepage:
    driver = None
    wpLib = None
    wpMenu = None

    def __init__(self, driver, wpLib):
        '''
        Init method.
        :param driver: Webdriver object
        :param wpLib: wpLib object for the helper class to get ids, classes, xpaths
        '''
        self.driver = driver
        self.wpLib = wpLib

        # Initialize the menu object
        self.wpMenu = WPMenu.WPMenu(self.driver, self.wpLib)

    def siteTitleElement(self):
        '''
        :return: The Webdriver element that refers to the site title.
        '''
        return self.driver.find_element_by_class_name(self.wpLib.siteTitle['class'])

    @property
    def siteTitle(self):
        '''
        :return: The text of the site title.
        '''
        siteTitleElement = self.driver.find_element_by_class_name(self.wpLib.siteTitle['class'])
        return siteTitleElement.text

    def siteDescriptionElement(self):
        '''
        :return: The Webdriver element that refers to the site description.
        '''
        return self.driver.find_element_by_class_name(self.wpLib.siteDescription['class'])

    @property
    def siteDescription(self):
        '''
        :return: The text of the site description.
        '''
        siteDescriptionElement = self.driver.find_element_by_class_name(self.wpLib.siteDescription['class'])
        return siteDescriptionElement.text

    def primaryMenuElement(self):
        '''
        :return: The Webdriver element that refers to the primary menu.
        '''
        return self.driver.find_element_by_id(self.wpLib.menuId)

    def contentAreaElement(self):
        '''
        :return: The Webdriver element that refers to the overall content area.
        '''
        return self.driver.find_element_by_id(self.wpLib.contentId)

    def primaryContentAreaElement(self):
        '''
        :return: The Webdriver element that refers to the primary content area.
        '''
        return self.driver.find_element_by_id(self.wpLib.primaryContentId)

    def secondaryContentAreaElement(self):
        '''
        :return: The Webdriver element that refers to the secondary content area.
        '''
        return self.driver.find_element_by_id(self.wpLib.secondaryContentId)

    def footerElement(self):
        '''
        :return: The Webdriver element that refers to the footer.
        '''
        return self.driver.find_element_by_id(self.wpLib.footerId)

    def footerSocialMenuElement(self):
        '''
        :return: The Webdriver element that refers to the footer social menu.
        '''
        return self.driver.find_element_by_id(self.wpLib.footerSocialMenuId)

    def footerSiteInfoElement(self):
        '''
        :return: The Webdriver element that refers to the footer site info section.
        '''
        return self.driver.find_element_by_class_name(self.wpLib.footerSiteInfoClass)