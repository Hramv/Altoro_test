from framework.elements.BaseElement import BaseElement


class Link(BaseElement):

    """
        A Link Class.
    """


    def __init__(self, locator: tuple, name: str):
        super().__init__(locator, name)


    def click(self):
        self.element.click()