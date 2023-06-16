from selenium.webdriver.common.by import By

from pages.elements_page import ElementsPage
from utils.UIObject import UIObject


class CheckBoxPage(ElementsPage):

    def __init__(self, driver):
        ElementsPage.__init__(self, driver)

        self.driver = driver
        self.__home_chevron = UIObject(By.CSS_SELECTOR, '[class="rct-text"] > [aria-label="Toggle"]')
        self.__desktop_chevron = UIObject(By.CSS_SELECTOR, '.rct-node-collapsed:nth-child(1) .rct-collapse')
        self.__documents_chevron = UIObject(By.CSS_SELECTOR, '.rct-node-parent:nth-child(2) .rct-collapse > .rct-icon')
        self.__downloads_chevron = UIObject(By.CSS_SELECTOR, '.rct-node:nth-child(3) .rct-collapse')
        self.__result = UIObject(By.CSS_SELECTOR, '[class="text-success"]')

    def expand_home_directory(self) -> None:
        self.__home_chevron.click()

    def expand_desktop_directory(self) -> None:
        self.__desktop_chevron.click()

    def expand_documents_directory(self) -> None:
        self.__documents_chevron.click()

    def expand_downloads_directory(self) -> None:
        self.__downloads_chevron.click()

    def select_checkbox(self, name) -> None:
        checkbox = UIObject(By.CSS_SELECTOR, f'label[for="tree-node-{name.lower()}"] > [class="rct-checkbox"]')
        checkbox.click()
        assert "check" in checkbox.get_attribute("class")

    def get_checkbox_text(self) -> list:
        results = []
        for element in self.__result.get_all_elements():
            results.append(element.text)
        return results
