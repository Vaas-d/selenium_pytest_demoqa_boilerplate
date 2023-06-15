import time

from selenium.webdriver.common.by import By

from pages.elements_page import ElementsPage
from pages.sidebar import Sidebar
from utils.UIObject import UIObject


class UploadAndDownloadPage(ElementsPage, Sidebar):

    def __init__(self, driver):
        ElementsPage.__init__(self, driver)
        Sidebar.__init__(self)

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
