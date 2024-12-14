from pages.AuthPage import AuthPage
from utils.Driver import Driver
import pytest

from time import sleep


class Parameters(object):
    """
    A Authorization Class that describes methods for testing login and 
    search forms on the auth. page Altoromutual.

    Attributes
    ----------            
    DEFAULT_USERS_DICT_URL     
    DEFAULT_PASSWORDS_DICT_URL
    TIME_OUT                    
    """

    DEFAULT_USERS_DICT_URL      = "tests/dicts/usernames.txt"
    DEFAULT_PASSWORDS_DICT_URL  = "tests/dicts/passwords.txt"
    TIME_OUT                    = 1
    ERROR_MESSAGE               = \
"Во время теста произошла не предвиденная ошибка.\
 Веб-ресурс Altoromutual скорее всего не доступен."


@pytest.fixture(scope="module")
def page():
    driver = Driver()
    page = AuthPage(driver=driver)
    yield page
    driver.quit()

@pytest.fixture()
def default_creds_dict():
    usernames = []
    passwords = []
    with open(Parameters.DEFAULT_USERS_DICT_URL, 'r') as u:
        for username in u:
            usernames.append(username.rstrip('\n'))
    with open(Parameters.DEFAULT_PASSWORDS_DICT_URL, 'r') as p:
        for password in p:
            passwords.append(password.rstrip('\n'))
    return (usernames, passwords)


def test_password_form_masking(page):
        
    """
    Testing the password form for characters masking
    
    """
    try:
        page.open()
        password_form_type = page.get_password_form().get_attribute("type")
    except:
        assert False, Parameters.ERROR_MESSAGE

    assert password_form_type == "password"


def test_default_creds(page, default_creds_dict):
        
    """
    Testing the presence of default accounts in the system.
    
    """
    
    default_creds = []

    try:
        for password in default_creds_dict[1]:
            for username in default_creds_dict[0]:
                page.open()
                sig_status = page.sign_in(username, password)
                if sig_status != page.LOGIN_FAILED_STATUS:
                    default_creds.append([username, password])
                    page.sign_off()
                sleep(Parameters.TIME_OUT)
    except:
        assert False, Parameters.ERROR_MESSAGE

    assert not default_creds