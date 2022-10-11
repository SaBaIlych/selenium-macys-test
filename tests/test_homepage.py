import time
import pytest
from pom.homepage_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:
    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)

        homepage_nav.get_tiny_box_close_button().click()
        
        for indx in range(8):
            homepage_nav.get_nav_links()[indx].click()
            time.sleep(1.5)

