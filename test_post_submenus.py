import WPPost
import pytest

# TestPostMenu
# Written by Angela Korra'ti
# Last updated 7/21/2023
#
# This class conducts tests against the submenus on a post of my test WordPress site.


@pytest.mark.usefixtures("setup_webdriver", "wp_lib")
class TestPostSubmenus:
    wp_menu = None

    def setup_method(self):
        """
        Do setup for the test cases.
        """
        self.driver.get(self.wp_lib.wp_post_uri)
        self.wp_menu = WPPost.WPPost(self.driver, self.wp_lib).wp_menu

    def test_home_submenu(self):
        """
        Verify all aspects of the Home submenu on a post
        """
        self.wp_menu.verify_home_submenu()

    def test_books_submenu(self):
        """
        Verify all aspects of the Books submenu on a post
        """
        self.wp_menu.verify_books_submenu()

    def test_faerie_submenu(self):
        """
        Verify the Faerie Blood item on the Books submenu on a post
        """
        self.wp_menu.verify_faerie_submenu()

    def test_bone_submenu(self):
        """
        Verify the Bone Walker item on the Books submenu on a post
        """
        self.wp_menu.verify_bone_submenu()

    def test_valor_submenu(self):
        """
        Verify the Valor of the Healer item on the Books submenu on a post
        """
        self.wp_menu.verify_valor_submenu()

    def test_vengeance_submenu(self):
        """
        Verify the Vengeance of the Hunter item on the Books submenu on a post
        """
        self.wp_menu.verify_vengeance_submenu()

    def test_victory_submenu(self):
        """
        Verify the Victory of the Hawk item on the Books submenu on a post
        """
        self.wp_menu.verify_victory_submenu()

    def test_short_submenu(self):
        """
        Verify the Short Stories item on the Books submenu on a post
        """
        self.wp_menu.verify_short_submenu()

    def test_store_submenu(self):
        """
        Verify the Store submenu on a post
        """
        self.wp_menu.verify_store_submenu()
