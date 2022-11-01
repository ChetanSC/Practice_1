from Config.Configdata import *
from Utilities.LoginPageUtilities import *
from Utilities.CommonPageUtilities import *


@pytest.mark.usefixtures("initiate_driver")
class TestLoginPage:

    def test_verify_login_with_correct_mail_and_password(self):
        LoginPageFunctions().sign_in_button()
        LoginPageFunctions().perform_login(correct_email, correct_passwd)
        verify_text = Util().find(pro)
        assert verify_text.text == "chetan prajapati", "Login was not successfull"

    def test_verify_login_with_correct_mail_and_wrong_password(self):
        LoginPageFunctions().sign_in_button()
        LoginPageFunctions().perform_login(correct_email, incorrect_passwd)
        incorrect_text = Util().find(incorrect)
        assert incorrect_text.text == "Authentication failed."

    def test_verify_login_with_wrong_email_and_correct_password(self):
        LoginPageFunctions().sign_in_button()
        LoginPageFunctions().perform_login(incorrect_email, correct_passwd)
        incorrect_text = Util().find(incorrect)
        assert incorrect_text.text == "Authentication failed."

    def test_verify_login_with_wrong_email_and_password(self):
        LoginPageFunctions().sign_in_button()
        LoginPageFunctions().perform_login(incorrect_email, incorrect_passwd)
        incorrect_text = Util().find(incorrect)
        assert incorrect_text.text == "Authentication failed."

    def test_verify_login_with_empty_email_and_correct_password(self):
        LoginPageFunctions().sign_in_button()
        LoginPageFunctions().perform_login(empty_email, correct_passwd)
        email_address = Util().find(invalid_email_adress)
        assert email_address.text == "An email address required."

    def test_verify_login_with_email_and_empty_password(self):
        LoginPageFunctions().sign_in_button()
        LoginPageFunctions().perform_login(correct_email, empty_passwd)
        passwd_address = Util.find(invalid_passwd_adress)
        assert passwd_address.text == "Password is required."

