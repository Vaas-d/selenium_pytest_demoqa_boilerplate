import time

import pytest

from pages.dynamic_elements_page import DynamicElementsPage
from utils.tools import take_screenshot


class TestDynamicElements:

    @pytest.fixture
    def test_setup(self, new_session):
        self.driver = new_session
        self.dynamic = DynamicElementsPage(self.driver)

        # click elements button on the homepage
        self.dynamic.click_elements_button()

        # click dynamic elements section from the sidebar
        self.dynamic.go_to_dynamic_props_section()

    @pytest.mark.regression
    def test_text_with_dynamic_id(self, test_setup):
        """Test to verify the functionality of the text field with dynamic id. The id should change each time the
        should become enabled after 5 seconds

        :param test_setup: setting up the browser and page objects
        :return: None
        """

        initial_id = self.dynamic.get_text_field_id()

        self.driver.refresh()

        new_id = self.dynamic.get_text_field_id()

        assert initial_id != new_id, f'Dynamic IDs should not match'

    # @mark.one
    @pytest.mark.regression
    def test_dynamic_button(self, test_setup):
        """Test to verify the functionality of the dynamic button. The button
        should become enabled after 5 seconds

        :param test_setup: setting up the browser and page objects
        :return: None
        """

        assert not self.dynamic.is_button_enabled(), f'The button is enabled'
        take_screenshot(self.driver, "dynamic_button_disabled")

        time.sleep(6)

        assert self.dynamic.is_button_enabled(), f'The button is not enabled'
        take_screenshot(self.driver, "dynamic_button_enabled")

    @pytest.mark.regression
    def test_changing_color_button(self, test_setup):
        """Test to verify the functionality of the button that changes inner text color. The inner text of the button
        should switch from back to red in 5 seconds

        :param test_setup: setting up the browser and page objects
        :return: None
        """

        initial_color = self.dynamic.get_button_inner_text_color_property()
        assert initial_color == "rgba(255, 255, 255, 1)"
        take_screenshot(self.driver, "dynamic_button_initial_color")

        time.sleep(6)

        new_color = self.dynamic.get_button_inner_text_color_property()
        assert new_color == "rgba(220, 53, 69, 1)"
        take_screenshot(self.driver, "dynamic_button_new_color")

    @pytest.mark.regression
    def test_appearing_button(self, test_setup):
        """Test to verify the functionality of the hidden button. The button
        should become visible after 5 seconds

        :param test_setup: setting up the browser and page objects
        :return: None
        """

        assert not self.dynamic.is_button_visible()
        take_screenshot(self.driver, "dynamic_button_invisible")

        self.dynamic.appearing_button().wait_to_appear()

        assert self.dynamic.is_button_visible()
        take_screenshot(self.driver, "dynamic_button_visible")
