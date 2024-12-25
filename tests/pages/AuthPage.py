from selenium.webdriver.common.by import By
from tests.const.Constants import AuthPageConst
from framework.pages.BasePage import BasePage
from framework.elements.Form import Form
from framework.elements.Button import Button
from framework.elements.TextElement import TextElement
from framework.elements.Link import Link


class AuthPageLocators():

    SEARCH_FORM         = (By.ID, 'query')
    USERNAME_FORM       = (By.ID, 'uid')
    PASSWORD_FORM       = (By.ID, 'passw')

    GO_BUTTON           = (By.CSS_SELECTOR, '[value="Go"]')
    LOGIN_BUTTON        = (By.NAME, 'btnSubmit')
    SIGNOFF_LINK        = (By.ID, 'LoginLink')

    SIGNIN_STATUS       = (By.CLASS_NAME, 'fl')
    SEARCH_RESULT       = (By.CLASS_NAME, 'fl')     
    DISCLAIMER          = (By.CLASS_NAME, 'disclaimer')


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
    sign_in(self, username: str, password: str) -> str
        Sign in the web-site and gets status.
    sign_off(self)
        Sign off the web-site.
    send_to_search_form(self, message) -> str
        Sends query for searching, and gets result.
    """


    def __init__(self):

        super().__init__(AuthPageConst.ALTORO_URL)

        self.search_form = Form(AuthPageLocators.SEARCH_FORM, "search_form")
        self.username_form = Form(AuthPageLocators.USERNAME_FORM, "username_form")
        self.password_form = Form(AuthPageLocators.PASSWORD_FORM, "password_form")
        self.go_button = Button(AuthPageLocators.GO_BUTTON, "go_button")
        self.login_button = Button(AuthPageLocators.LOGIN_BUTTON, "login_button")
        self.signoff_link = Link(AuthPageLocators.SIGNOFF_LINK, "signoff_link")
        self.signin_status = TextElement(AuthPageLocators.SIGNIN_STATUS, "signin_status")
        self.search_result = TextElement(AuthPageLocators.SEARCH_RESULT, "search_result")
        self.disclaimer = TextElement(AuthPageLocators.DISCLAIMER, "disclaimer")

        
    def sign_in(self, username: str, password: str):
        
        self.username_form.get()
        self.username_form.send(username)
        self.password_form.get()
        self.password_form.send(password)
        self.login_button.get()
        self.login_button.click()

        self.signin_status.get()


        return self.signin_status.get_text()
    

    def sign_off(self):

        self.signoff_link.get()
        self.signoff_link.click()

    
    def send_to_search_form(self, message):
        
        self.search_form.get()
        self.search_form.send(message)
        self.go_button.get()
        self.go_button.click()

        self.search_result.get()

        return self.search_result.get_text()


    