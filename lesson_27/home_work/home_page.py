from domain_credentials import *
from elem_processing import *
from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):

        self.driver = driver
        self.driver.implicitly_wait(5)
        self.url = f'https://{login}:{passwd}@qauto.forstudy.space/'

        # Header navigation locators
        self.signin_button = (By.XPATH, "//div/button[@class='btn btn-outline-white header_signin']")
        self.guest_login_button = (By.XPATH, "//button[text()='Guest log in']")

        # Page locators
        self.signup_button = (By.XPATH, "//button[text()='Sign up']")

        # Contact social links locators
        self.facebook_link = (By.XPATH, "//span[@class='socials_icon icon icon-facebook']")
        self.telegram_link = (By.XPATH, "//span[@class='socials_icon icon icon-telegram']")
        self.youtube_link = (By.XPATH, "//span[@class='socials_icon icon icon-youtube']")
        self.instagram_link = (By.XPATH, "//span[@class='socials_icon icon icon-instagram']")
        self.linkedin_link = (By.XPATH, "//span[@class='socials_icon icon icon-linkedin']")

    # Click page buttons
    def click_sign_up(self):
        """Open sign up frame"""

        self.driver.get(self.url)
        signup_button = find(self.driver, *self.signup_button)
        click_button(self.driver, signup_button)

    # Click header menu buttons
    def click_sign_in(self):
        """Open sign in frame"""

        self.driver.get(self.url)
        signin_button = find(self.driver, *self.signin_button)
        click_button(self.driver, signin_button)

    def click_signin_guest(self):
        """Sign in with guest rights"""

        self.driver.get(self.url)
        signin_guest_button = find(self.driver, *self.guest_login_button)
        click_button(self.driver, signin_guest_button)

    # Click social media buttons
    def click_facebook(self):
        """Click to facebook icon link"""

        self.driver.get(self.url)
        facebook = find(self.driver, *self.facebook_link)
        click_button(self.driver, facebook)

    def click_telegram(self):
        """Click to telegram icon link"""

        self.driver.get(self.url)
        telegram = find(self.driver, *self.telegram_link)
        click_button(self.driver, telegram)

    def click_youtube(self):
        """Click to youtube icon link"""

        self.driver.get(self.url)
        youtube = find(self.driver, *self.youtube_link)
        click_button(self.driver, youtube)

    def click_instagram(self):
        self.driver.get(self.url)
        """Click to instagram icon link"""

        instagram = find(self.driver, *self.instagram_link)
        click_button(self.driver, instagram)

    def click_linkedin(self):
        """Click to linkedin icon link"""

        self.driver.get(self.url)
        linkedin = find(self.driver, *self.linkedin_link)
        click_button(self.driver, linkedin)

    # Waits for elements to be located
    def wait_for_signup_button(self):
        """Wait for Signup button"""

        wait_element_to_be_located(self.driver, self.signup_button)


class LoginFrame(HomePage):
    def __init__(self, driver):
        super().__init__(driver)

        # Sign Up frame locators
        self.signup_name_input = (By.ID, "signupName")
        self.signup_lastname_input = (By.ID, "signupLastName")
        self.signup_email_input = (By.ID, "signupEmail")
        self.signup_password_input = (By.ID, "signupPassword")
        self.signup_reenter_password_input = (By.ID, "signupRepeatPassword")
        self.register_button = (By.XPATH, "//button[text()='Register']")

        # Sign In frame locators
        self.signin_email_input = (By.ID, "signinEmail")
        self.signin_password_input = (By.ID, "signinPassword")
        self.login_button = (By.XPATH, "//button[text()='Login']")
        self.error_frame = (By.XPATH, "//p[text()='Wrong email or password']")

    # Sign Up frame actions
    def signup_enter_name(self, name):
        """Enter data to name input"""
        name_input = find(self.driver, *self.signup_name_input)
        enter_text(self.driver, name_input, name)

    def signup_enter_lastname(self, lastname):
        """Enter data last name input"""

        last_name_input = find(self.driver, *self.signup_lastname_input)
        enter_text(self.driver, last_name_input, lastname)

    def signup_enter_email(self, email):
        """Enter data to email input"""

        email_input = find(self.driver, *self.signup_email_input)
        enter_text(self.driver, email_input, email)

    def signup_enter_password(self, password):
        """Enter data password input"""

        password_input = find(self.driver, *self.signup_password_input)
        enter_text(self.driver, password_input, password)

    def signup_reenter_password(self, re_password):
        """Confirm password in reenter password input"""

        re_password_input = find(self.driver, *self.signup_reenter_password_input)
        enter_text(self.driver, re_password_input, re_password)

    def click_register(self):
        """Confirm register frame"""
        register_button = find(self.driver, *self.register_button)
        click_button(self.driver, register_button)

    # Sign In frame actions
    def signin_enter_email(self, email):
        """Enter email to email input"""

        email_input = find(self.driver, *self.signin_email_input)
        enter_text(self.driver, email_input, email)

    def signin_enter_password(self, password):
        """Enter password to password input"""

        password_input = find(self.driver, *self.signin_password_input)
        enter_text(self.driver, password_input, password)

    def click_login(self):
        """Confirm login frame"""

        login_button = find(self.driver, *self.login_button)
        click_button(self.driver, login_button)

    # Waits for elements to be located
    def wait_for_error_frame(self):
        """Wait for error frame"""

        wait_element_to_be_located(self.driver, self.error_frame)
