from selenium.webdriver.common.by import By

from pages.elements_page import ElementsPage
from utils.UIObject import UIObject


class TextBoxPage(ElementsPage):

    def __init__(self, driver):
        ElementsPage.__init__(self, driver)

        self.driver = driver
        # input form
        self.__full_name_input = UIObject(By.CSS_SELECTOR, '[id="userName"]')
        self.__email_input = UIObject(By.CSS_SELECTOR, '[id="userEmail"]')
        self.__current_address_input = UIObject(By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
        self.__permanent_address_input = UIObject(By.CSS_SELECTOR, 'textarea[id="permanentAddress"]')
        self.__submit_btn = UIObject(By.CSS_SELECTOR, 'button[id="submit"]')
        # output form
        self.__output_form = UIObject(By.CSS_SELECTOR, 'div[id="output"]')
        self.__name_field = UIObject(By.CSS_SELECTOR, 'p[id="name"]')
        self.__email_field = UIObject(By.CSS_SELECTOR, 'p[id="email"]')
        self.__current_address_field = UIObject(By.CSS_SELECTOR, 'p[id="currentAddress"]')
        self.__permanent_address_field = UIObject(By.CSS_SELECTOR, 'p[id="permanentAddress"]')

    def set_username(self, user_name) -> None:
        self.__full_name_input.set_text(user_name)

    def set_email(self, email) -> None:
        self.__email_input.set_text(email)

    def set_current_address(self, address) -> None:
        self.__current_address_input.set_text(address)

    def set_permanent_address(self, address) -> None:
        self.__permanent_address_input.set_text(address)

    def submit_form(self) -> None:
        self.__submit_btn.click()
        self.__output_form.wait_to_appear()

    def get_username(self) -> str:
        return self.__name_field.get_text()

    def get_user_email(self) -> str:
        return self.__email_field.get_text()

    def get_current_address(self) -> str:
        return self.__current_address_field.get_text()

    def get_permanent_address(self) -> str:
        return self.__permanent_address_field.get_text()
