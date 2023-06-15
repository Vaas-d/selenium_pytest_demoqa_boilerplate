import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from exceptions import ElementNotFoundError
from utils.BrowserManager import Browser


class UIObject:

    def __init__(self, by, locator):

        self.by = by
        self.locator = locator

    def get_element(self, wait=60):
        self.wait_to_appear(wait)
        return Browser.get_driver().find_element(self.by, self.locator)

    def get_all_elements(self, wait=60):
        self.wait_to_appear(wait)
        return Browser.get_driver().find_elements(self.by, self.locator)

    def get_locator(self) -> str:
        return self.locator

    def get_text(self, encoding=None) -> str:
        text = self.get_element().text
        return text.encode(encoding) if encoding else text

    def get_attribute(self, value) -> str:
        return self.get_element().get_attribute(value)

    def get_css_property(self, value) -> str:
        return self.get_element().value_of_css_property(value)

    def is_selected(self) -> bool:
        return self.get_element().is_selected()

    def is_checked(self) -> bool:
        return Browser.get_driver().execute_script("return arguments[0].checked;", self.get_element())

    def exists(self, timeout: int = 1) -> bool:
        try:
            WebDriverWait(Browser.get_driver(), timeout).until(EC.presence_of_element_located((self.by, self.locator)))
            return True
        except ElementNotFoundError:
            return False

    def is_clickable(self) -> bool:

        def is_clickable(by, locator) -> bool:
            try:
                WebDriverWait(Browser.get_driver(), 1).until(EC.element_to_be_clickable((by, locator)))
                return True
            except:
                return False

        return self.exists() and is_clickable(self.by, self.locator)

    def wait_to_be_clickable(self, seconds=60, ignore_error=False):
        start = time.time()
        while (time.time() - start) < seconds:
            if self.is_clickable():
                return self
            time.sleep(1)
        if not ignore_error:
            if self.exists():
                raise AssertionError(f"Locator {self.locator} is in the DOM: but did not become click-able in {seconds}"
                                     f" seconds")
            raise AssertionError(f"Locator {self.locator} is not in the DOM and so not click-able")
        else:
            return self

    def wait_to_appear(self, seconds=30, ignore_error=False):
        start = time.time()
        while (time.time() - start) < seconds:
            if self.exists():
                return self
        if not ignore_error:
            raise AssertionError(f"Locator: {self.locator} did not appear in {seconds} seconds!")
        else:
            return self

    def wait_to_disappear(self, seconds, ignore_error=False):
        while self.exists():
            try:
                WebDriverWait(Browser.get_driver(), seconds, 1).until(
                    EC.invisibility_of_element_located((self.by, self.locator)))
            except Exception as error:
                if not ignore_error:
                    raise AssertionError(
                        f"Locator: {self.locator} did not disappear in {seconds} seconds! Error: {error.message}")
        return self

    def click(self, wait=60, double_click=False, right_click=False):
        self.wait_to_be_clickable(wait)
        initial_handles = Browser.get_driver().window_handles

        try:
            if double_click:
                actions = ActionChains(Browser.get_driver())
                actions.double_click(self.get_element()).perform()
            elif right_click:
                actions = ActionChains(Browser.get_driver())
                actions.context_click(self.get_element()).perform()
            else:
                self.get_element().click()
        except Exception as error:
            if "Other element would receive the click" in error.message:
                self.scroll_into_center()
                if double_click:
                    actions = ActionChains(Browser.get_driver())
                    actions.double_click(self.get_element()).perform()
                elif right_click:
                    actions = ActionChains(Browser.get_driver())
                    actions.context_click(self.get_element()).perform()
                else:
                    self.get_element().click()
            else:
                raise error

        if len(Browser.get_driver().window_handles) > len(initial_handles):
            Browser.switch_to_latest_active_window()
        return self

    def set_text(self, value, loose_focus=False):
        self.get_element().clear()
        self.get_element().send_keys(str(value))
        if loose_focus:
            self.press_key(Keys.TAB)
        return self

    def scroll_into_center(self):
        scrollElementIntoMiddle = \
            "var viewPortHeight = Math.max(document.documentElement.clientHeight, " \
            "window.innerHeight || 0); var elementTop = arguments[0].getBoundingClientRect().top;" \
            "window.scrollBy(0, elementTop-(viewPortHeight/2));"

        Browser.get_driver().execute_script(scrollElementIntoMiddle, self.get_element())

    def scroll_into_view(self):
        Browser.get_driver().execute_script("arguments[0].scrollIntoView()", self.get_element())
        return self

    def send_value(self, value):
        self.get_element().send_keys(value)
        return self

    def press_key(self, key, use_action_chains=False):
        if not use_action_chains:
            self.get_element().send_keys(key)
        else:
            chains = ActionChains(driver=Browser.get_driver())
            chains.send_keys(key).perform()
        return self

    def mouse_over(self):
        ui_object = self.get_element()
        ActionChains(Browser.get_driver()).move_to_element(ui_object).perform()
        return self
