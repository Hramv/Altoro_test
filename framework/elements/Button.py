from framework.elements.BaseElement import BaseElement


class Button(BaseElement):

    """
        A Button Class.
    """


    def __init__(self, locator: tuple, name: str):
        super().__init__(locator, name)