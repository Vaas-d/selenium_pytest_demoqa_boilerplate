from selenium.webdriver.common.by import By

from pages.elements_page import ElementsPage
from utils.UIObject import UIObject


class WebTablePage(ElementsPage):

    def __init__(self, driver):
        ElementsPage.__init__(self, driver)

        self.driver = driver

        self.__add_button = UIObject(By.CSS_SELECTOR, '[id="addNewRecordButton"]')

        # registration form
        self.__modal_title = UIObject(By.CSS_SELECTOR, '[id="registration-form-modal"]')
        self.__first_name_input = UIObject(By.CSS_SELECTOR, '[id="firstName"]')
        self.__last_name_input = UIObject(By.CSS_SELECTOR, '[id="lastName"]')
        self.__email_input = UIObject(By.CSS_SELECTOR, '[id="userEmail"]')
        self.__age_input = UIObject(By.CSS_SELECTOR, '[id="age"]')
        self.__salary_input = UIObject(By.CSS_SELECTOR, '[id="salary"]')
        self.__department_input = UIObject(By.CSS_SELECTOR, '[id="department"]')
        self.__submit_btn = UIObject(By.CSS_SELECTOR, '[id="submit"]')

        # web table
        self.__table_row = UIObject(By.CSS_SELECTOR, 'div[role="rowgroup"]')

    def add_new_user(self, first_name, last_name, email, age, salary, department) -> None:
        self.__click_add_button()
        self.__modal_title.wait_to_appear()
        self.__enter_first_name(first_name)
        self.__enter_last_name(last_name)
        self.__enter_email(email)
        self.__enter_age(age)
        self.__enter_salary(salary)
        self.__enter_department(department)
        self.__submit_form()

    def __click_add_button(self) -> None:
        self.__add_button.click()

    def __enter_first_name(self, value) -> None:
        self.__first_name_input.wait_to_appear()
        self.__first_name_input.set_text(value)

    def __enter_last_name(self, value) -> None:
        self.__last_name_input.wait_to_appear()
        self.__last_name_input.set_text(value)

    def __enter_email(self, value) -> None:
        self.__email_input.wait_to_appear()
        self.__email_input.set_text(value)

    def __enter_age(self, value) -> None:
        self.__age_input.wait_to_appear()
        self.__age_input.set_text(value)

    def __enter_salary(self, value) -> None:
        self.__salary_input.wait_to_appear()
        self.__salary_input.set_text(value)

    def __enter_department(self, value) -> None:
        self.__department_input.wait_to_appear()
        self.__department_input.set_text(value)

    def __submit_form(self) -> None:
        self.__submit_btn.click()

    def get_row_text(self) -> tuple:
        rows_data = self.__table_row.get_all_elements()
        rows_data.reverse()
        for row in rows_data:
            if "       " not in row.text:
                return row.text.split("\n")
