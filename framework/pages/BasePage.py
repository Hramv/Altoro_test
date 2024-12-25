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
        self.init_webdriver()
        self._url = page_url


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_webdriver()


    def init_webdriver(self):
        self._driver = Driver()


    def close_webdriver(self):
        self._driver.close()


    def open(self):
        self._driver.open_page(self._url)       
    
      