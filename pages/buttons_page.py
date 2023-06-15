from selenium.webdriver.common.by import By

from pages.elements_page import ElementsPage
from pages.sidebar import Sidebar
from utils.UIObject import UIObject


class ButtonsPage(ElementsPage, Sidebar):

    def __init__(self, driver):
        ElementsPage.__init__(self, driver)
        Sidebar.__init__(self)

        self.driver = driver

        self.__double_click_btn = UIObject(By.CSS_SELECTOR, 'button[id="doubleClickBtn"]')
        self.__right_click_btn = UIObject(By.CSS_SELECTOR, 'button[id="rightClickBtn"]')
        self.__dynamic_btn = UIObject(By.XPATH, '//button[text()="Click Me"]')
        self.__double_click_msg = UIObject(By.CSS_SELECTOR, 'p[id="doubleClickMessage"]')
        self.__right_click_msg = UIObject(By.CSS_SELECTOR, 'p[id="rightClickMessage"]')
        self.__dynamic_click_msg = UIObject(By.CSS_SELECTOR, 'p[id="dynamicClickMessage"]')

    def perform_double_click(self) -> None:
        self.__double_click_btn.click(double_click=True)

    def get_double_click_message(self) -> str:
        self.__double_click_msg.wait_to_appear()
        return self.__double_click_msg.get_text()

    def perform_rmb_click(self) -> None:
        self.__right_click_btn.click(right_click=True)

    def get_rmb_click_message(self) -> str:
        self.__right_click_msg.wait_to_appear()
        return self.__right_click_msg.get_text()

    def perform_dynamic_click(self) -> None:
        self.__dynamic_btn.click()

    def get_dynamic_click_message(self) -> str:
        self.__dynamic_click_msg.wait_to_appear()
        return self.__dynamic_click_msg.get_text()
