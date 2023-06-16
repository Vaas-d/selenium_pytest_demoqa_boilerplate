from pages.homepage import HomePage
from pages.sidebar import Sidebar


class ElementsPage(HomePage, Sidebar):

    def __init__(self, driver):
        HomePage.__init__(self, driver)
        Sidebar.__init__(self)


