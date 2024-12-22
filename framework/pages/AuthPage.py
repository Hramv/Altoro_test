from selenium.webdriver.common.by import By
from framework.const.Constants import AuthPageConst
from framework.pages.BasePage import BasePage
from framework.elements.Form import Form
from framework.elements.Button import Button
from framework.elements.TextElement import TextElement
from framework.elements.Link import Link


class AuthPageLocators():

    SEARCH_FORM         = (By.ID, "query")
    USERNAME_FORM       = (By.ID, "uid")
    PASSWORD_FORM       = (By.ID, "passw")

    GO_BUTTON           = (By.CSS_SELECTOR, '[value="Go"]')
    LOGIN_BUTTON        = (By.NAME, "btnSubmit")
    SIGNOFF_LINK        = (By.ID, "LoginLink")

    SIGNIN_STATUS       = (By.CLASS_NAME, "fl")
    SEARCH_RESULT       = (By.CLASS_NAME, "fl")     #(by=By.TAG_NAME, value="p")


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

        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_webdriver()