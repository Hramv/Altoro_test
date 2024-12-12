from pages.AuthPage import AuthPage
from utils.Driver import Driver
import pytest

from time import sleep


class Parameters(object):
    TEST_SITE_URL               = "http://www.altoromutual.com/login.jsp"
    DEFAULT_USERS_DICT_URL      = "tests/dicts/usernames.txt"
    DEFAULT_PASSWORDS_DICT_URL  = "tests/dicts/passwords.txt"
    TIME_OUT                    = 0.5


@pytest.fixture(scope="module")
def page():
    driver = Driver()
    page = AuthPage(driver=driver, url=Parameters.TEST_SITE_URL)
    yield page
    driver.quit()

@pytest.fixture()
def creds_dict():
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
    page.open()
    assert page.get_password_form().get_attribute("type") == "password"


def test_default_creds(page, creds_dict):
    
    default_creds = []

    for password in creds_dict[1]:
        for username in creds_dict[0]:
            page.open()
            sig_status = page.sign_in(username, password)
            if sig_status != page.LOGIN_FAILED_STATUS:
                default_creds.append([username, password])
                page.sign_off()
            sleep(Parameters.TIME_OUT)

    assert not default_creds