from selenium.webdriver.common.by import By
from utils.UIObject import UIObject


class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.__homepage_page_title = UIObject(By.CSS_SELECTOR, 'a[href="https://demoqa.com"]')
        self.__elements_button = UIObject(By.CSS_SELECTOR, 'div.home-body > div > div:nth-child(1)')
        self.__forms_button = UIObject(By.CSS_SELECTOR, 'div.home-body > div > div:nth-child(2)')
        self.__alerts_button = UIObject(By.CSS_SELECTOR, 'div.home-body > div > div:nth-child(3)')
        self.__widgets_button = UIObject(By.CSS_SELECTOR, 'div.home-body > div > div:nth-child(4)')
        self.__interactions_button = UIObject(By.CSS_SELECTOR, 'div.home-body > div > div:nth-child(6)')
        self.__bookstore_button = UIObject(By.CSS_SELECTOR, 'div.home-body > div > div:nth-child(6)')

    def click_elements_button(self) -> None:
        self.__homepage_page_title.wait_to_appear()
        self.__elements_button.wait_to_appear()
        self.__elements_button.scroll_into_view()
        self.__elements_button.click()

    def click_forms_button(self) -> None:
        self.__homepage_page_title.wait_to_appear()
        self.__forms_button.wait_to_appear()
        self.__forms_button.scroll_into_view()
        self.__forms_button.click()

    def click_alerts_button(self) -> None:
        self.__homepage_page_title.wait_to_appear()
        self.__alerts_button.wait_to_appear()
        self.__alerts_button.scroll_into_view()
        self.__alerts_button.click()

    def click_widgets_button(self) -> None:
        self.__homepage_page_title.wait_to_appear()
        self.__widgets_button.wait_to_appear()
        self.__widgets_button.scroll_into_view()
        self.__widgets_button.click()

    def click_interactions_button(self) -> None:
        self.__homepage_page_title.wait_to_appear()
        self.__interactions_button.wait_to_appear()
        self.__interactions_button.scroll_into_view()
        self.__interactions_button.click()

    def click_bookstore_button(self) -> None:
        self.__homepage_page_title.wait_to_appear()
        self.__bookstore_button.wait_to_appear()
        self.__bookstore_button.scroll_into_view()
        self.__bookstore_button.click()
