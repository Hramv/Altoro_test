from framework.utils.Driver import Driver
from framework.const.Constants import PageConst


class BaseElement():

    """
        A BaseElement Class.
    """


    def __init__(self, locator: tuple, name: str,):

        self._locator = locator
        self.name = name


    def get(self):

        self.element = Driver.find_element(self._locator, self.name)
        return self.element
        

    def get_attribute(self, attribute: str):
        
        element_attribute = self.element.get_attribute(attribute)
        return element_attribute
    

    def get_text(self):
        return self.element.text
    

    def click(self):
        self.element.click()
