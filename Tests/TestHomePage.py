from Config.Configdata import *
from Utilities.HomePageUtilities import HomePageFunctions
from Utilities.LoginPageUtilities import *
from Utilities.CommonPageUtilities import Util


@pytest.mark.usefixtures("initiate_driver")
class TestHomePage:
    @pytest.mark.smoke
    def test_final_order(self):
        LoginPageFunctions().sign_in_button()
        LoginPageFunctions().perform_login(correct_email, correct_passwd)
        HomePageFunctions().final_order()
        verify_text = Util().find(order_placed)
        assert verify_text.text == "Your order on My Store is complete.", 'Order not placed.'

    def test_click_contact_us(self):
        LoginPageFunctions().sign_in_button()
        LoginPageFunctions().perform_login(correct_email, correct_passwd)
        HomePageFunctions().click_contact_us()
        verify_text = Util().find(customer_service)
        assert verify_text.text == "CUSTOMER SERVICE - CONTACT US"

    def test_click_sign_out(self):
        LoginPageFunctions().sign_in_button()
        LoginPageFunctions().perform_login(correct_email, correct_passwd)
        HomePageFunctions().view_cart()
        HomePageFunctions().click_sign_out()
        verify_text = Util().find(sign_in)
        assert verify_text.text == "Sign in"
