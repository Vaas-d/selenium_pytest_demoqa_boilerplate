from selenium.webdriver.common.by import By

from pages.elements_page import ElementsPage
from utils.UIObject import UIObject


class DynamicElementsPage(ElementsPage):

    def __init__(self, driver):
        ElementsPage.__init__(self, driver)

        self.driver = driver

        self.__text_with_random_id = UIObject(By.XPATH, '//p[text()="This text has random Id"]')
        self.__enable_after_5sec_button = UIObject(By.CSS_SELECTOR, 'button[id="enableAfter"]')
        self.__color_change_button = UIObject(By.CSS_SELECTOR, 'button[id="colorChange"]')
        self.__visible_after_5sec_button = UIObject(By.CSS_SELECTOR, 'button[id="visibleAfter"]')

    def is_button_enabled(self) -> bool:
        return self.__enable_after_5sec_button.is_clickable()

    def get_button_inner_text_color_property(self) -> str:
        return self.__color_change_button.get_css_property('color')

    def get_text_field_id(self) -> str:
        return self.__text_with_random_id.get_attribute("id")

    def is_button_visible(self) -> bool:
        return self.__visible_after_5sec_button.exists()

    def appearing_button(self) -> UIObject:
        return self.__visible_after_5sec_button
