from time import sleep
from tests.const.Constants import AuthPageConst
from framework.utils.Logger import Logger
from framework.utils.Driver import Driver


def test_password_form_masking(auth_page):
        
    """
    Testing the password form for characters masking
    
    """

    url = AuthPageConst.ALTORO_AUTH_URL

    auth_page.open(AuthPageConst.ALTORO_AUTH_URL)
    if not auth_page.is_opened(AuthPageConst.ALTORO_AUTH_URL):
        assert False, f"An error occurred while trying to load the page\
 {AuthPageConst.ALTORO_AUTH_URL}."
    else:
        Logger.debug(f"Page {AuthPageConst.ALTORO_AUTH_URL} loaded.") 

    auth_page.password_form.get()
    password_form_type = auth_page.password_form.get_attribute("type")

    assert password_form_type == "password"


def test_default_creds(auth_page, default_creds_dict):
        
    """
    Testing the presence of default accounts in the system.
    
    """
    
    default_creds = []
    
    for password in default_creds_dict[1]:
        for username in default_creds_dict[0]:

            auth_page.open(AuthPageConst.ALTORO_AUTH_URL)
            if not auth_page.is_opened(AuthPageConst.ALTORO_AUTH_URL):
                assert False, f"An error occurred while trying to load the page\
 {AuthPageConst.ALTORO_AUTH_URL}."
                
            auth_page.sign_in(username, password)
            if auth_page.login_success():
                default_creds.append([username, password])
                Logger.debug(f"Page {AuthPageConst.ALTORO_MAIN_URL} loaded.") 
                auth_page.sign_off()

            elif auth_page.login_failed():
                Logger.debug(f"Page {AuthPageConst.ALTORO_AUTH_URL} loaded.")
            else:
                assert False, f"An error occurred while trying to load the page\
 {AuthPageConst.ALTORO_AUTH_URL}."

            Driver.reload()
            sleep(AuthPageConst.TIME_OUT)
    
    assert not default_creds