from framework.elements.BaseElement import BaseElement


class TextElement(BaseElement):

    """
        A TextElement Class.
    """


    def __init__(self, locator: tuple, name: str):
        super().__init__(locator, name)


    def get_text(self):
        return self.element.text