from framework.elements.BaseElement import BaseElement


class Form(BaseElement):

    """
        A Form Class.
    """


    def __init__(self, locator: tuple, name: str):
        super().__init__(locator, name)


    def send(self, message: str):
        self.element.send_keys(message)