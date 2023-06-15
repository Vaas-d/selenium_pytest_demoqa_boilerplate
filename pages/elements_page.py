from selenium.webdriver.common.by import By

from pages.homepage import HomePage
from pages.sidebar import Sidebar
from utils.UIObject import UIObject


class ElementsPage(HomePage, Sidebar):

    def __init__(self, driver):
        HomePage.__init__(self, driver)
        Sidebar.__init__(self)

        self.__page_title = UIObject(By.CSS_SELECTOR, 'div[class="main-header"]')

    def get_elements_page_title(self) -> str:
        return self.__page_title.get_text()
