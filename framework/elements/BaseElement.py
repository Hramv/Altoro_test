from framework.utils.Driver import Driver


class BaseElement():

    """
        A BaseElement Class.
    """


    def __init__(self, locator: tuple, name: str):
        self._driver = Driver()
        self._locator = locator
        self.name = name


    def get(self):
        self.element = self._driver.find_element(self._locator)
        

    def get_attribute(self, attribute: str):
        return self.element.get_attribute(attribute)
