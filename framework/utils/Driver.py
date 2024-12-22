from framework.utils.Singletone import singleton
from framework.utils.Drivers_builders import Builder
from framework.const.Constants import BrowserConst

@singleton
class Driver():

    """
        A Driver Class. 
    """

    def __init__(self, executable_path: str=BrowserConst.EXECUTABEL_PATH):

        match BrowserConst.BROWSER:
            case BrowserConst.FIREFOX:
                self._driver = Builder.firefox_driver(executable_path)
            case BrowserConst.CHROME:
                self._driver = Builder.chrome_driver(executable_path)
            case BrowserConst.EDGE:
                self._driver = Builder.edge_driver(executable_path)
            case _:
                raise ValueError(
    f"{BrowserConst.BROWSER} is not supported. Cannot build WebDriver.")


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


    def open_page(self, url, load_time):
        self._driver.get(url)
        self._driver.implicitly_wait(load_time)


    def find_element(self, locator):
        self._driver.find_element(locator)

    
    def close(self):
        self._driver.quit()


    


    