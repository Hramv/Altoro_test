from framework.utils.Singletone import SingletonMeta
from framework.utils.Drivers_builders import Builder
from framework.utils.Logger import Logger
from framework.const.Constants import PageConst

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Driver(metaclass=SingletonMeta):

    """
        A Driver Class. 
    """

    def __init__(self):

        self._driver = Builder.builder()

    @staticmethod
    def get_instance():
        
        return Driver._instances[Driver]

    @staticmethod
    def open_page(url):

        self = Driver.get_instance()

        try:
            self._driver.get(url)
        except:
            Logger.error(f"An error occurred while trying to load the page {url}.")
            self.close()

    @staticmethod
    def find_element(locator: tuple, name: str):

        self = Driver.get_instance()

        element = WebDriverWait(self._driver, PageConst.LOAD_TIME).\
                       until(EC.presence_of_element_located(locator), \
                       message=f"Еlement {name} with {locator} locator is not found.")
        if element:
            Logger.debug(f"Еlement {name} with {locator} locator is found.")
        return element
    
    @staticmethod
    def close():

        self = Driver.get_instance()
        self._driver.quit()

    @staticmethod
    def reload():
        
        self = Driver.get_instance()
        self.close()
        self.__init__()


    


    