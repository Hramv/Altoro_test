from framework.utils.Driver import Driver


class BaseElement():

    """
        A BaseElement Class.
    """


    def __init__(self, locator: tuple, name: str, timeout: int=1):

        self._driver = Driver()
        self._locator = locator
        self.name = name
        self._timeout = timeout


    def get(self):

        self.element = self._driver.find_element(self._locator, self.name, self._timeout)
        return self.element
        

    def get_attribute(self, attribute: str):
        
        element_attribute = self.element.get_attribute(attribute)
        return element_attribute
