from ideas_for_test.hillel_test_api.hillel_api import auth
from ideas_for_test.hillel_test_api.hillel_api import users
from ideas_for_test.hillel_test_api.hillel_api import s
from home_page import HomePage
from home_page import LoginFrame
from selenium import webdriver
import pytest


@pytest.fixture()
def new_user():
    """Register a test user using API then remove"""
    # create user
    register_data = {
        "name": "Anatolii",
        "lastName": "Pepsi",
        "email": "apepsii@test.com",
        "password": "Qam2608venv#",
        "repeatPassword": "Qam2608venv#"
    }
    auth.signup(s, register_data)
    yield

    # delete user
    users.users(s)


@pytest.fixture()
def logged_user(driver):
    """Register a new user using API. Then User logins by selenium webdriver.
    Then user will be removed using API"""

    # Create user using API
    register_data = {
        "name": "Anatolii",
        "lastName": "Pepsi",
        "email": "apepsii@test.com",
        "password": "Qam2608venv#",
        "repeatPassword": "Qam2608venv#"
    }
    auth.signup(s, register_data)

    # Login using browser
    home_page = HomePage(driver)
    home_page.click_sign_in()

    user_email = register_data.get("email")
    user_pass = register_data.get("password")

    login_frame = LoginFrame(driver)
    login_frame.signin_enter_email(user_email)
    login_frame.signin_enter_password(user_pass)
    login_frame.click_login()

    yield

    # Login with API and remove user
    login_data = {
        "email": user_email,
        "password": user_pass,
    }
    auth.signin(s, login_data)
    users.users(s)


@pytest.fixture(scope="function")
def remove_user():
    """Login then delete test user using API"""
    request_body = {
        "email": "aaaatestw@gmail.com",
        "password": "123Abc+-=",
        }
    auth.signin(s, request_body)
    users.users(s)


@pytest.fixture
def driver():
    """Create google Chrome webdriver"""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
