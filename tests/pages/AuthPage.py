from selenium.webdriver.common.by import By

class AuthPage():

    """
    A Authorization Class that describes methods for testing login and 
    search forms on the auth. page Altoromutual.
    """

    LOGIN_FAILED_STATUS = "Login Failed: We're sorry, but this username or \
password was not found in our system. Please try again."

    def __init__(self, driver: object, url: str):
        self._driver = driver
        self._url = url


    def open(self):
        self._driver.get(self._url)
        self._driver.implicitly_wait(0.5)  
    

    def get_search_form(self):
        return self._driver.find_element(by=By.ID, value="query")
    
    def get_go_button(self):
        return self._driver.find_element(by=By.CSS_SELECTOR, value='[value="Go"]')

    def get_search_result(self):
        search_div = self._driver.find_element(by=By.CLASS_NAME, value="fl")
        return search_div.find_element(by=By.TAG_NAME, value="p")


    def get_username_form(self):
        return self._driver.find_element(by=By.ID, value="uid")
    
    def get_password_form(self):
        return self._driver.find_element(by=By.ID, value="passw")
    
    def get_login_button(self):
        return self._driver.find_element(by=By.NAME, value="btnSubmit")
    
    def get_sign_in_status(self):
        status = self._driver.find_element(by=By.CLASS_NAME, value="fl").\
                            find_element(by=By.TAG_NAME, value="p")
        if not status: 
            status = self._driver.find_element(by=By.CLASS_NAME, value="fl").\
                             find_element(by=By.TAG_NAME, value="h1")
        return status
    

    def send_to_search_form(self, message):

        self.get_search_form().send_keys(message)
        self.get_go_button().click()

        return self.get_search_result().text
    

    def sign_in(self, username: str, password: str):
        
        self.get_username_form().send_keys(username)
        self.get_password_form().send_keys(password)
        self.get_login_button().click()

        return self.get_sign_in_status().text
    

    def sign_off(self):
        self._driver.find_element(by=By.ID, value="LoginLink").click()
    
      