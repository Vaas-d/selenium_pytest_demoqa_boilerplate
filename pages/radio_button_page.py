from selenium.webdriver.common.by import By

from pages.elements_page import ElementsPage
from utils.UIObject import UIObject


class RadioButtonsPage(ElementsPage):

    def __init__(self, driver):
        ElementsPage.__init__(self, driver)

        self.driver = driver

        self.__result_text_field = UIObject(By.CSS_SELECTOR, '[class="text-success"]')

    def select_radio_button(self, name) -> None:
        radio_button = UIObject(By.CSS_SELECTOR, f'label[for="{name.lower()}Radio"]')
        radio_button.click()

    def get_result_message(self) -> str:
        self.__result_text_field.wait_to_appear()
        return self.__result_text_field.get_text()
