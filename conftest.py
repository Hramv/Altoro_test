import pytest

from tests.pages.AuthPage import AuthPage
from tests.const.Constants import TestConst
from framework.utils.Logger import Logger


@pytest.fixture(scope="module")
def auth_page():
    Logger.set_level(10)      #DEBUG 10, INFO 20
    auth_page = AuthPage()
    yield auth_page
    auth_page.close_webdriver()

@pytest.fixture()
def default_creds_dict():
    usernames = []
    passwords = []
    with open(TestConst.DEFAULT_USERS_DICT_URL, 'r') as u:
        for username in u:
            usernames.append(username.rstrip('\n'))
    with open(TestConst.DEFAULT_PASSWORDS_DICT_URL, 'r') as p:
        for password in p:
            passwords.append(password.rstrip('\n'))
    return (usernames, passwords)