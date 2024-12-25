from framework.utils.Singletone import singleton
from framework.utils.Drivers_builders import Builder
from framework.const.Constants import BrowserConst
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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


    def open_page(self, url):
        self._driver.get(url)


    def find_element(self, locator: tuple, timeout: int):
        element = WebDriverWait(self._driver, timeout).\
                       until(EC.presence_of_element_located(locator), \
                       message=f"Еlement not found.")
        return element
    

    def close(self):
        self._driver.quit()


    


    