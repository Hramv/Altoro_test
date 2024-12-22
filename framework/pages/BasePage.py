from framework.utils.Driver import Driver
from framework.const.Constants import PageConst

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


    def init_webdriver(self):
        self._driver = Driver()


    def close_webdriver(self):
        self._driver.close() 


    def open(self):
        self._driver.get(self._url)
        self._driver.implicitly_wait(PageConst.LOAD_TIME)
        
    
      