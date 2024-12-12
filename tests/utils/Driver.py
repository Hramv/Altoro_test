from utils.Singletone import singleton
from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.firefox.service import Service


@singleton
class Driver(Firefox):

    """
    A Driver Class.
    """
    
    def __init__(self):
        service = Service(executable_path="/usr/local/bin/geckodriver")
        options = FirefoxOptions()
        super().__init__(service=service, options=options)