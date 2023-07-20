# WPTestLib
# Written by Angela Korra'ti
# Last updated 7/19/2023
#
# This is a helper class to contain various test strings, ids, classes, and XPaths.


class WPTestLib:
    def __init__(self, protocol=None, host=None):
        if protocol is not None:
            self.protocol = protocol
        if host is not None:
            self.host = host
        self.wp_base_uri = self.wp_base_uri % (self.protocol, self.host)
        self.wp_post_uri = self.wp_base_uri + self.wp_post_uri

    # These values are all top-level things about the site and the Selenium hub
    selenium_host = "http://localhost:4444/wd/hub"
    protocol = "http"
    host = "wordpress.local"
    wp_base_uri = "%s://%s/"
    site_title = {"class": "site-title", "text": "Anna's Dev Wordpress"}
    site_description = {"class": "site-description", "text": "Just another WordPress site"}
    page_title_class = "page-title"
    entry_title_class = "entry-title"

    # Strings for test Uris
    wp_post_uri = "/2016/09/13/testing-testing-testing-is-this-thing-on/"
    post_title = "Testing, testing, testing, is this thing on?"

    # Strings pertaining to the main content areas.
    content_id = "content"
    primary_content_id = "primary"
    secondary_content_id = "secondary"
