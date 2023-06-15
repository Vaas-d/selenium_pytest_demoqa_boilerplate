import os

import pytest

from utils.BrowserManager import Browser
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope='function')
def new_session():
    Browser.create_new_driver()
    driver = Browser.get_driver()
    driver.get(os.getenv("BASE_URL"))
    yield driver
    Browser.shutdown()
