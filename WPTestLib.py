# WPTestLib
# Written by Angela Korra'ti
# Last updated 2/7/2019
#
# This is a helper class to contain various test strings, ids, classes, and xpaths.

class WPTestLib:
    def __init__(self, protocol=None, host=None):
        if (protocol != None):
            self.protocol = protocol
        if (host != None):
            self.host = host
        self.wpBaseUri = self.wpBaseUri % (self.protocol, self.host)

    # These values are all top-level things about the site and the Selenium hub
    seleniumHost="http://localhost:4444/wd/hub"
    protocol="http"
    host="wordpress.local"
    wpBaseUri = "%s://%s"
    siteTitle = {"class":"site-title", "text":"Anna's Dev Wordpress"}
    siteDescription = {"class":"site-description", "text":"Just another WordPress site"}

    # Strings pertaining to the main content areas.
    contentId="content"
    primaryContentId="primary"
    secondaryContentId="secondary"

    # Strings pertaining to the footer.
    footerId="colophon"
    footerSocialMenuId="menu-social-1"
    footerSiteInfoClass="site-info"
    footerSiteTitleXPath="//span[@class='site-title']/a"
    footerWPLinkXPath="//div[@class='site-info']/a"
    footerWPLink="https://wordpress.org/"
    footerWPLinkText="Proudly powered by Wordpress"
    footerSocialFacebookXPath="//ul[@id='menu-social-1']/li[1]/a"
    footerSocialFacebookLink="https://www.facebook.com/annathepiper"
    footerSocialFacebookText="Facebook"
    footerSocialTwitterXPath="//ul[@id='menu-social-1']/li[2]/a"
    footerSocialTwitterLink="https://twitter.com/annathepiper"
    footerSocialTwitterText="Twitter"
    footerSocialGithubXPath="//ul[@id='menu-social-1']/li[3]/a"
    footerSocialGithubLink="https://github.com/annathepiper"
    footerSocialGithubText="GitHub"
    footerSocialLinkedInXPath="//ul[@id='menu-social-1']/li[4]/a"
    footerSocialLinkedInLink="https://www.linkedin.com/in/angela-korrati"
    footerSocialLinkedInText="LinkedIn"

    # These are all strings pertaining to primary menu items.
    menuId="menu-primary"
    menuHome = {"XPath":"//*[@id='menu-primary']/li[1]/a", "text":"Home", "link":"http://wordpress.local/"}
    menuAbout = {"XPath":"//*[@id='menu-primary']/li[2]/a", "About":"http://wordpress.local/about/"}
    menuBooks = {"XPath":"//*[@id='menu-primary']/li[3]/a", "text":"Books", "link":"http://wordpress.local/books/"}
    menuBlog = {"XPath":"//*[@id='menu-primary']/li[4]/a", "text":"Blog", "link":"http://wordpress.local/blog/"}
    menuContact = {"XPath":"//*[@id='menu-primary']/li[5]/a", "text":"Contact",
                   "link":"http://wordpress.local/contact/"}
    menuStore = {"XPath":"//*[@id='menu-primary']/li[6]/a", "text":"Store",
                 "link":"https://squareup.com/market/angela-korrati"}

    # Secondary menu items for the Home menu
    submenuHome = {"XPath":"//*[@id='menu-primary']/li[1]/ul/li/a", "text":"Angelahighland.com",
                   "link":"http://www.angelahighland.com/"}

    # Secondary menu items for the Books menu
    submenuBooksXPath="//*[@id='menu-primary']/li[3]/ul"
    submenuFaerie = {"XPath":"//*[@id='menu-primary']/li[3]/ul/li[1]/a", "text":"Faerie Blood",
                     "link":"http://wordpress.local/books/faerie-blood/"}
    submenuBone = {"XPath":"//*[@id='menu-primary']/li[3]/ul/li[2]/a", "text":"Bone Walker",
                   "link":"http://wordpress.local/books/bone-walker/"}
    submenuValorXPath="//*[@id='menu-primary']/li[3]/ul/li[3]/a"
    submenuValorText="Valor of the Healer"
    submenuValorLink="http://wordpress.local/books/valor-of-the-healer/"
    submenuVengeanceXPath="//*[@id='menu-primary']/li[3]/ul/li[4]/a"
    submenuVengeanceText="Vengeance of the Hunter"
    submenuVengeanceLink="http://wordpress.local/books/vengeance-of-the-hunter/"
    submenuVictoryXPath="//*[@id='menu-primary']/li[3]/ul/li[5]/a"
    submenuVictoryText="Victory of the Hawk"
    submenuVictoryLink="http://wordpress.local/books/victory-of-the-hawk/"
    submenuShortXPath="//*[@id='menu-primary']/li[3]/ul/li[6]/a"
    submenuShortText="Short Stories"
    submenuShortLink="http://wordpress.local/books/short-stories/"

    # Secondary menu items for the Store menu
    submenuStoreXPath="//*[@id='menu-primary']/li[6]/ul/li/a"
    submenuStoreText="Bone Walker: The Free Court of Seattle Soundtrack"
    submenuStoreLink="http://wordpress.local/bone-walker-the-free-court-of-seattle-soundtrack/"