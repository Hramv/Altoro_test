

class BrowserConst():

    BROWSER = "firefox"
    EXECUTABEL_PATH = "/usr/local/bin/geckodriver"
    
    FIREFOX = "firefox"
    CHROME  = "chrome"
    EDGE    = "edge"


class PageConst():

    LOAD_TIME   = 1 #sec


class AuthPageConst():

    AUTH_TIME_OUT   = 1     #sec
    ALTORO_URL          = "http://www.altoromutual.com/login.jsp"
    LOGIN_FAILED_STATUS = "Login Failed: We're sorry, but this username or \
password was not found in our system. Please try again."


class TestConst():

    DEFAULT_USERS_DICT_URL      = "tests/dicts/usernames.txt"
    DEFAULT_PASSWORDS_DICT_URL  = "tests/dicts/passwords.txt"
    ERROR_MESSAGE               = \
"Во время теста произошла не предвиденная ошибка.\
 Веб-ресурс Altoromutual скорее всего не доступен."