import os

import pytest

from pages.links_page import LinksPage
from data.test_data import TestData
from utils.tools import take_screenshot
from dotenv import load_dotenv

load_dotenv()


class TestLinks:

    @pytest.fixture
    def test_setup(self, new_session):
        self.driver = new_session
        self.links = LinksPage(self.driver)

        # click elements button on the homepage
        self.links.click_elements_button()

        # click links section from the sidebar
        self.links.go_to_links_section()

    @pytest.mark.smoke
    def test_home_link(self, test_setup):
        """Test to validate home link on the page

        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.links.click_home_link()

        assert self.driver.current_url == os.getenv("BASE_URL")
        take_screenshot(self.driver, "new_tab")

    @pytest.mark.smoke
    def test_dynamic_link(self, test_setup):
        """Test to validate dynamic link on the page

        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.links.click_dynamic_link()

        assert self.driver.current_url == os.getenv("BASE_URL")
        take_screenshot(self.driver, "new_tab_dynamic_link")

    @pytest.mark.smoke
    def test_created_link(self, test_setup):
        """Test to validate created link on the page and verify response

        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.links.click_created_link()

        text = self.links.get_link_response()

        assert text == TestData.responses["Created"]

        take_screenshot(self.driver, "Created")

    @pytest.mark.smoke
    def test_no_content_link(self, test_setup):
        """Test to validate no content link on the page and verify response

        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.links.click_no_content_link()

        text = self.links.get_link_response()

        assert text == TestData.responses["No Content"]

        take_screenshot(self.driver, "No Content")

    @pytest.mark.smoke
    def test_moved_link(self, test_setup):
        """Test to validate moved link on the page and verify response

        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.links.click_moved_link()

        text = self.links.get_link_response()

        assert text == TestData.responses["Moved"]

        take_screenshot(self.driver, "Moved")

    @pytest.mark.smoke
    def test_bad_request_link(self, test_setup):
        """Test to validate bad request link on the page and verify response

        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.links.click_bad_request_link()

        text = self.links.get_link_response()

        assert text == TestData.responses["Bad Request"]

        take_screenshot(self.driver, "Bad Request")

    @pytest.mark.smoke
    def test_unauthorized_link(self, test_setup):
        """Test to validate unauthorized link on the page and verify response

        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.links.click_unauthorized_link()

        text = self.links.get_link_response()

        assert text == TestData.responses["Unauthorized"]

        take_screenshot(self.driver, "Unauthorized")

    @pytest.mark.smoke
    def test_forbidden_link(self, test_setup):
        """Test to validate forbidden link on the page and verify response

        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.links.click_forbidden_link()

        text = self.links.get_link_response()

        assert text == TestData.responses["Forbidden"]

        take_screenshot(self.driver, "Forbidden")

    @pytest.mark.smoke
    def test_not_found_link(self, test_setup):
        """Test to validate not found link on the page and verify response

        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.links.click_not_found_link()

        text = self.links.get_link_response()

        assert text == TestData.responses["Not Found"]

        take_screenshot(self.driver, "Not Found")
