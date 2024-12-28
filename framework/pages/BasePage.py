from framework.utils.Driver import Driver


class BasePage():

    """
    A BasePage Class that describes basic methods for testing Altoromutual.

    Attributes
    ----------

    Methods
    -------
    __init__(self, driver: object)
        Instance initiation.
    open(self)
       Opens web-site page.     
    """


    def __init__(self, page_url:str):
        self._url = page_url


    def open(self, url: str):
       Driver.open_page(url)       
    
      