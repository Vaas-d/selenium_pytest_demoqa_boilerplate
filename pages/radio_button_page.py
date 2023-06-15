from selenium.webdriver.common.by import By

from pages.elements_page import ElementsPage
from pages.sidebar import Sidebar
from utils.UIObject import UIObject


class RadioButtonsPage(ElementsPage, Sidebar):

    def __init__(self, driver):
        ElementsPage.__init__(self, driver)
        Sidebar.__init__(self)

        self.driver = driver

        self.__result = UIObject(By.CSS_SELECTOR, '[class="text-success"]')

    def select_radio_button(self, name) -> None:
        radio_button = UIObject(By.CSS_SELECTOR, f'label[for="{name.lower()}Radio"]')
        radio_button.click()

    def get_result_message(self) -> str:
        self.__result.wait_to_appear()
        return self.__result.get_text()
