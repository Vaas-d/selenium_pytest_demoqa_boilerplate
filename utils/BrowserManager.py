import threading

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from definitions import ROOT_DIR


class Browser:

    __DRIVER_MAP = {}

    @staticmethod
    def create_new_driver():

        thread_object = threading.current_thread()

        def get_driver():
            options = webdriver.ChromeOptions()
            # options.add_argument("--headless=new")  # Don't forget to enable before pushing to the repo
            options.add_argument("--window-size=1920x1080")
            options.add_argument("--disable-gpu")
            options.add_argument("--incognito")
            options.add_argument("ignore-certificate-errors")
            options.add_argument("--ignore-ssl-errors")
            options.add_argument("--disable-infobars")
            options.add_argument("--ignore-certificate-errors-spki-list")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-plugins-discovery")
            options.add_argument("--start-maximized")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
            prefs = {"download.default_directory": f"{ROOT_DIR}\\data",
                     "profile.default_content_settings": {"images": 2}}
            options.add_experimental_option("prefs", prefs)
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

            return driver

        Browser.__map(thread_object, get_driver())
        return Browser.get_driver()

    @staticmethod
    def get_driver():
        return Browser.__DRIVER_MAP[threading.current_thread()]["driver"]

    @staticmethod
    def shutdown():
        Browser.get_driver().quit()

    @staticmethod
    def __map(thread, driver):
        Browser.__DRIVER_MAP[thread] = {"driver": driver}

    @staticmethod
    def get_driver_map():
        return Browser.__DRIVER_MAP

    @staticmethod
    def switch_to_latest_active_window():
        windows = Browser.get_driver().window_handles
        if len(windows) == 1:
            Browser.get_driver().switch_to.window(windows[0])
            return
        for index in range(1, len(windows)):
            Browser.get_driver().switch_to.window(windows[-index])
            return

    @staticmethod
    def close_window():
        Browser.get_driver().close()
