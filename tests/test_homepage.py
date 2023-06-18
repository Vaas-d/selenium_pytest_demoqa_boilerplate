import pytest

from pages.homepage import HomePage
from data.test_data import TestData
from utils.tools import take_screenshot


class TestHomepage:

    @pytest.fixture
    def test_setup(self, new_session):
        self.driver = new_session
        self.home = HomePage(self.driver)

    @pytest.mark.smoke
    def test_navigation_to_homepage(self, test_setup):
        actual_text = self.home.get_homepage_banner_text()
        assert actual_text == TestData.homepage_bunner_text
        take_screenshot(self.driver, "Homepage")
