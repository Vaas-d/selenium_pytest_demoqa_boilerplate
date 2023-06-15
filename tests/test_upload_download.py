import os

import pytest

from pages.upload_and_download_page import UploadAndDownloadPage
from definitions import ROOT_DIR
from utils.tools import take_screenshot

file_path = f'{ROOT_DIR}/data/sampleFile.jpeg'


class TestTextBoxes:

    @pytest.fixture
    def test_setup(self, new_session):
        self.driver = new_session
        self.manage_file = UploadAndDownloadPage(self.driver)

        # click elements button on the homepage
        self.manage_file.click_elements_button()

        # click test boxes section from the sidebar
        self.manage_file.go_to_upload_section()

        yield
        # remove downloaded file (crucial clean up for local test runs)
        if os.path.isfile(file_path):
            os.remove(f'{ROOT_DIR}/data/sampleFile.jpeg')

    def test_upload_file(self, test_setup):
        """Test to verify the uploading a file

        :param test_setup: setting up the browser and page objects
        :return: None
        """
        self.manage_file.upload_file(f"{ROOT_DIR}/data/test_data.py")

        file_path = self.manage_file.get_uploaded_file_path()

        assert "test_data.py" in file_path

        take_screenshot(self.driver, "uplaoded_file")

    def test_download_file(self, test_setup):
        """Test to verify downloading a file

        :param test_setup: setting up the browser and page objects
        :return: None
        """
        self.manage_file.download_file()

        try:
            with open(file_path, 'rb') as image:
                image.read()
        except FileNotFoundError as err_:
            raise FileNotFoundError(err_)
