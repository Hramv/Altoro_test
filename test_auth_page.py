from time import sleep
from tests.const.Constants import TestConst, AuthPageConst


def test_password_form_masking(auth_page):
        
    """
    Testing the password form for characters masking
    
    """

    try:
        auth_page.open()
        auth_page.password_form.get()
        password_form_type = auth_page.password_form.get_attribute("type")
    except:
        assert False, TestConst.ERROR_MESSAGE

    assert password_form_type == "password"


def test_default_creds(auth_page, default_creds_dict):
        
    """
    Testing the presence of default accounts in the system.
    
    """
    
    default_creds = []

    try:
        for password in default_creds_dict[1]:
            for username in default_creds_dict[0]:
                auth_page.open()
                sig_status = auth_page.sign_in(username, password)
                if sig_status.find(AuthPageConst.LOGIN_FAILED_STATUS) == -1:
                    default_creds.append([username, password])
                    auth_page.sign_off()
                sleep(AuthPageConst.TIME_OUT)
    except:
        assert False, TestConst.ERROR_MESSAGE

    assert not default_creds