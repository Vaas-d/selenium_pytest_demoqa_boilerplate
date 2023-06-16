import time

from selenium.webdriver.common.by import By

from pages.elements_page import ElementsPage
from utils.UIObject import UIObject


class UploadAndDownloadPage(ElementsPage):

    def __init__(self, driver):
        ElementsPage.__init__(self, driver)

        self.driver = driver

        self.__download_button = UIObject(By.CSS_SELECTOR, 'a[id="downloadButton"]')
        self.__upload_button = UIObject(By.CSS_SELECTOR, 'input[id="uploadFile"]')

        self.__uploaded_file_path = UIObject(By.CSS_SELECTOR, 'p[id="uploadedFilePath"]')

    def upload_file(self, file) -> None:
        self.__upload_button.send_value(file)

    def get_uploaded_file_path(self) -> str:
        return self.__uploaded_file_path.get_text()

    def download_file(self) -> None:
        self.__download_button.click()
        time.sleep(3)
