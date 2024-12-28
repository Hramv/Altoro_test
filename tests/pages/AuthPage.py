from selenium.webdriver.common.by import By

from tests.const.Constants import AuthPageConst
from framework.pages.BasePage import BasePage
from framework.elements.TextBox import TextBox
from framework.elements.Button import Button
from framework.elements.TextElement import TextElement
from framework.elements.Link import Link
from framework.utils.Logger import Logger


class AuthPageLocators():

    SEARCH_FORM         = (By.ID, 'query')
    USERNAME_FORM       = (By.ID, 'uid')
    PASSWORD_FORM       = (By.ID, 'passw')

    GO_BUTTON           = (By.CSS_SELECTOR, '[value="Go"]')
    LOGIN_BUTTON        = (By.NAME, 'btnSubmit')
    SIGNOFF_LINK        = (By.ID, 'LoginLink')

    DIV_RESULT          = (By.CLASS_NAME, 'fl') 
    INDEX_PAGE_LINK     = (By.LINK_TEXT, 'Online Banking with FREE Online Bill Pay')


class AuthPage(BasePage):

    """
    A Authorization Class that describes methods for testing login and 
    search forms on the auth. page Altoromutual.

    Attributes
    ----------

    Methods
    -------
    __init__(self, driver: object)
        Instance initiation.
    is_opened(self, url)
        Checks whether the page has opened.     
    sign_in(self, username: str, password: str) -> str
        Sign in the web-site.
    get_sign_in_result(self)
        Gets sigin result.
    sign_off(self)
        Sign off the web-site.
    login_failed(self)
        Checks if login faled.
    login_succes(self)
        Check if login was successful.
    send_to_search_form(self, message) -> str
        Sends query for searching, and gets result.
    """


    def __init__(self):

        super().__init__(AuthPageConst.ALTORO_AUTH_URL)

        self.search_form = TextBox(AuthPageLocators.SEARCH_FORM, "search_form")
        self.username_form = TextBox(AuthPageLocators.USERNAME_FORM, "username_form")
        self.password_form = TextBox(AuthPageLocators.PASSWORD_FORM, "password_form")
        self.go_button = Button(AuthPageLocators.GO_BUTTON, "go_button")
        self.login_button = Button(AuthPageLocators.LOGIN_BUTTON, "login_button")
        self.signoff_link = Link(AuthPageLocators.SIGNOFF_LINK, "signoff_link")
        self.div_result = TextElement(AuthPageLocators.DIV_RESULT, "div_result")
        self.index_page_link = Link(AuthPageLocators.INDEX_PAGE_LINK, "index_page_link")


    def is_opened(self, url):
        
        match url:
            case AuthPageConst.ALTORO_AUTH_URL:
                self.username_form.get()
                Logger.debug(f"Page {AuthPageConst.ALTORO_AUTH_URL} loaded.")
                return True
            case AuthPageConst.ALTORO_INDEX_URL:
                self.index_page_link.get()
                Logger.debug(f"Page {AuthPageConst.ALTORO_INDEX_URL} loaded.")
                return True
            case AuthPageConst.ALTORO_MAIN_URL:
                self.div_result.get()
                Logger.debug(f"Page {AuthPageConst.ALTORO_MAIN_URL} loaded.")
                return True
        

    def sign_in(self, username: str, password: str):
        
        self.username_form.get()
        self.username_form.send(username)
        self.password_form.get()
        self.password_form.send(password)
        self.login_button.get()
        self.login_button.click()
    

    def get_sign_in_result(self):

        self.div_result.get()
        
        return self.div_result.get_text()
      

    def sign_off(self):

        self.signoff_link.get()
        self.signoff_link.click()


    def login_failed(self):

        sig_status = self.get_sign_in_result()
        return sig_status.find(AuthPageConst.LOGIN_FAILED_STATUS) != -1


    def login_success(self):

        sig_status = self.get_sign_in_result()
        return sig_status.find(AuthPageConst.LOGIN_SUCCES_STATUS) != -1  

    
    def send_to_search_form(self, message: str):
        
        self.search_form.get()
        self.search_form.send(message)
        self.go_button.get()
        self.go_button.click()

        self.div_result.get()

        return self.div_result.get_text()


    