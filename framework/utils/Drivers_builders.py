
from selenium.webdriver import Firefox, FirefoxOptions, Chrome, ChromeOptions,\
                                Edge, EdgeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService

from framework.const.Constants import BrowserConst


class Builder():

    """
        Driver builder class.
    """

    @staticmethod
    def firefox_driver(executable_path: str=None):

        """
        A Firefox Driver initialization method.
        """
        
        service = FirefoxService(executable_path=executable_path)
        options = FirefoxOptions()
        return Firefox(service=service, options=options)

    @staticmethod
    def chrome_driver(executable_path: str=None):

        """
        A Chrome Driver initialization method.
        """
        
        service = ChromeService(executable_path=executable_path)
        options = ChromeOptions()
        return Chrome(service=service, options=options)

    @staticmethod
    def edge_driver(executable_path: str=None):

        """
        A Edge Driver initialization method.
        """

        service = EdgeService(executable_path=executable_path)
        options = EdgeOptions()
        return Edge(service=service, options=options)
    
    @staticmethod
    def builder(executable_path: str=BrowserConst.EXECUTABEL_PATH):

        """
        WebDriver Builder.
        """

        match BrowserConst.BROWSER:
            case BrowserConst.FIREFOX:
                return Builder.firefox_driver(executable_path)
            case BrowserConst.CHROME:
                return Builder.chrome_driver(executable_path)
            case BrowserConst.EDGE:
                return Builder.edge_driver(executable_path)
            case _:
                error_message = f"{BrowserConst.BROWSER} is not supported. Cannot build WebDriver."
                Logger.error(error_message)
                raise ValueError(error_message)