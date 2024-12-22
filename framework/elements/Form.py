from framework.elements.BaseElement import BaseElement


class Form(BaseElement):

    """
        A Form Class.
    """


    def __init__(self, locator: tuple, name: str):
        super().__init__(locator, name)


    def send(self):
        self.element.send_keys()