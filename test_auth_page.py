from time import sleep
from tests.const.Constants import TestConst, AuthPageConst
from framework.utils.Logger import Logger


def test_password_form_masking(auth_page):
        
    """
    Testing the password form for characters masking
    
    """

    auth_page.open()
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
            auth_page.open()
            sig_status = auth_page.sign_in(username, password)

            if sig_status.find(AuthPageConst.LOGIN_SUCCES_STATUS) != -1:
                default_creds.append([username, password])
                Logger.debug(f"Page {AuthPageConst.ALTORO_AUTH_URL} loaded.") 
                auth_page.sign_off()
            elif sig_status.find(AuthPageConst.LOGIN_FAILED_STATUS) != -1:
                Logger.debug(f"Page {AuthPageConst.ALTORO_MAIN_URL} loaded.")
            else:
                Logger.debug(f"An error occurred while trying to load the page.")
                assert False

            sleep(AuthPageConst.TIME_OUT)
    
    assert not default_creds