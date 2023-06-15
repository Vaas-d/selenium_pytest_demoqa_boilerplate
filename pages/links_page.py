import time

from selenium.webdriver.common.by import By

from pages.elements_page import ElementsPage
from pages.sidebar import Sidebar
from utils.UIObject import UIObject


class LinksPage(ElementsPage, Sidebar):

    def __init__(self, driver):
        ElementsPage.__init__(self, driver)
        Sidebar.__init__(self)

        self.driver = driver

        self.__home_link = UIObject(By.CSS_SELECTOR, 'a[id="simpleLink"]')
        self.__dynamic_link = UIObject(By.CSS_SELECTOR, 'a[id="dynamicLink"]')

        # API links
        self.__created_link = UIObject(By.CSS_SELECTOR, 'a[id="created"]')
        self.__no_content_link = UIObject(By.CSS_SELECTOR, 'a[id="no-content"]')
        self.__moved_link = UIObject(By.CSS_SELECTOR, 'a[id="moved"]')
        self.__bad_request_link = UIObject(By.CSS_SELECTOR, 'a[id="bad-request"]')
        self.__unauthorized_link = UIObject(By.CSS_SELECTOR, 'a[id="unauthorized"]')
        self.__forbidden_link = UIObject(By.CSS_SELECTOR, 'a[id="forbidden"]')
        self.__not_found_link = UIObject(By.CSS_SELECTOR, 'a[id="invalid-url"]')

        self.__link_response = UIObject(By.CSS_SELECTOR, 'p[id="linkResponse"]')

    def click_home_link(self) -> None:
        self.__home_link.click()

    def click_dynamic_link(self) -> None:
        self.__dynamic_link.click()

    def click_created_link(self) -> None:
        self.__created_link.click()

    def click_no_content_link(self) -> None:
        self.__no_content_link.click()

    def click_moved_link(self) -> None:
        self.__moved_link.click()

    def click_bad_request_link(self) -> None:
        self.__bad_request_link.click()

    def click_unauthorized_link(self) -> None:
        self.__unauthorized_link.click()

    def click_forbidden_link(self) -> None:
        self.__forbidden_link.click()

    def click_not_found_link(self) -> None:
        self.__not_found_link.click()

    def get_link_response(self) -> str:
        return self.__link_response.get_text()
