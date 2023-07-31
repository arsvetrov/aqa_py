from home_page import HomePage
from home_page import LoginFrame
from garage_page import GaragePage
from garage_page import Navigation
import pytest


@pytest.mark.positive
def test_register_user(driver, remove_user):
    """Register a new user"""

    home_page = HomePage(driver)
    home_page.click_sign_up()

    login_frame = LoginFrame(driver)
    login_frame.signup_enter_name("Anatolii")
    login_frame.signup_enter_lastname("Pepsi")
    login_frame.signup_enter_email("aaaatestw@gmail.com")
    login_frame.signup_enter_password("123Abc+-=")
    login_frame.signup_reenter_password("123Abc+-=")
    login_frame.click_register()

    dashboard_page = GaragePage(driver)
    dashboard_page.wait_for_register_frame()

    assert driver.current_url == dashboard_page.url
    assert "Registration complete" in driver.page_source
    assert " My profile " in driver.page_source


@pytest.mark.positive
def test_login01(new_user, driver):
    """Existing user login"""

    home_page = HomePage(driver)
    home_page.click_sign_in()

    login_frame = LoginFrame(driver)
    login_frame.signin_enter_email("apepsii@test.com")
    login_frame.signin_enter_password("Qam2608venv#")
    login_frame.click_login()

    garage_page = GaragePage(driver)
    garage_page.wait_for_login_frame()

    assert driver.current_url == garage_page.url
    assert "You have been successfully logged in" in driver.page_source
    assert " My profile " in driver.page_source


@pytest.mark.negative
def test_login02(driver):
    """Login not existing user"""

    home_page = HomePage(driver)
    home_page.click_sign_in()

    login_frame = LoginFrame(driver)
    login_frame.signin_enter_email("pepsi@test.com")
    login_frame.signin_enter_password("Qam2608venv#")
    login_frame.click_login()
    login_frame.wait_for_error_frame()

    assert driver.current_url == login_frame.url
    assert "Wrong email or password" in driver.page_source


@pytest.mark.positive
def test_guest_signin(driver):
    """Try to sign in as guest"""
    login_page = HomePage(driver)
    login_page.click_signin_guest()

    garage_page = GaragePage(driver)
    garage_page.wait_for_guest_frame()

    assert driver.current_url == garage_page.url
    assert "Logged in as guest, any changes will be lost!" in driver.page_source
    assert " My profile " in driver.page_source


@pytest.mark.positive
def test_logout(driver, new_user):
    """User logout"""
    login_page = HomePage(driver)
    login_page.click_sign_in()

    login_frame = LoginFrame(driver)
    login_frame.signin_enter_email("apepsii@test.com")
    login_frame.signin_enter_password("Qam2608venv#")
    login_frame.click_login()

    navigation = Navigation(driver)
    navigation.click_logout()

    login_page.wait_for_signup_button()

    assert driver.current_url == login_page.url
    assert "Sign up" in driver.page_source
    assert "Do more!" in driver.page_source
