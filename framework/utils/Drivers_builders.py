
from selenium.webdriver import Firefox, FirefoxOptions, Chrome, ChromeOptions,\
                                Edge, EdgeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService


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