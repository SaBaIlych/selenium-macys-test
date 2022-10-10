import time
import pytest
from pom.homepage_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:
    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        expected_links_text = homepage_nav.NAV_LINK_TEXT

        actual_links_text  = homepage_nav.get_nav_links_text()

        assert actual_links_text == expected_links_text, 'Validating Nav Links text'
        
        homepage_nav.get_tiny_box_close_button().click()
        
        for indx in range(8):
            homepage_nav.get_nav_links()[indx].click()
            homepage_nav.driver.delete_all_cookies()
            time.sleep(3)
