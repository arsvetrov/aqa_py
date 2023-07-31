from selenium.webdriver.common.by import By
from elem_processing import *
from domain_credentials import *


class GaragePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)
        self.url = f"https://{login}:{passwd}@qauto.forstudy.space/panel/garage"

        # Page info frames locators
        self.success_login_frame = (By.XPATH, "//*[contains(text(), 'logged in')]")
        self.success_register_frame = (By.XPATH, "//p[text()='Registration complete']")
        self.guest_frame = (By.XPATH, "//*[contains(text(), 'Logged in as guest')]")

        # Page buttons locators
        self.add_car_button = (By.XPATH, "//button[text()='Add car']")

    def click_add_car(self):
        add_button = find(self.driver, *self.add_car_button)
        click_button(self.driver, add_button)

    def wait_for_login_frame(self):
        """Wait for successful login frame """
        wait_element_to_be_located(self.driver, self.success_login_frame)

    def wait_for_guest_frame(self):
        """Wait for guest mode frame"""
        wait_element_to_be_located(self.driver, self.guest_frame)

    def wait_for_register_frame(self):
        """Wait for successful registration frame"""
        wait_element_to_be_located(self.driver, self.success_register_frame)


class Navigation(GaragePage):

    def __init__(self, driver):
        super().__init__(driver)

        # Side menu locators
        self.logout_button = (By.XPATH, "//a[@class='btn btn-link text-danger btn-sidebar sidebar_btn'"
                                        " and text()=' Log out ']")

        # Main menu locators
        self.garage_link = (By.XPATH, "//a[@class='btn header-link -active' and text()='Garage']")
        self.fuel_expenses_link = (By.XPATH, "//a[@class='btn header-link' and text()='Fuel expenses']")
        self.instructions_link = (By.XPATH, "//a[@class='btn header-link' and text()='Instructions']")
        self.profile_button = (By.XPATH, "//div/button[@class='dropdown-toggle user-nav_toggle']")

        # Profile drop-down menu locators
        self.garage_link_drop = (By.XPATH, "//a[@class='dropdown-item btn btn-link user-nav_link disabled'"
                                           " and text()='Garage']")
        self.fuel_expenses_link_drop = (By.XPATH, "//a[@class='dropdown-item btn btn-link user-nav_link'"
                                                  " and text()='Fuel expenses']")
        self.instructions_link_drop = (By.XPATH, "//a[@class='dropdown-item btn btn-link user-nav_link'"
                                                 " and text()='Instructions']")
        self.profile_link_drop = (By.XPATH, "//a[@class='dropdown-item btn btn-link user-nav_link'"
                                            " and text()='Profile']")
        self.settings_link_drop = (By.XPATH, "//a[@class='dropdown-item btn btn-link user-nav_link'"
                                             " and text()='Settings']")
        self.logout_link_drop = (By.XPATH, "//a[@class='dropdown-item btn btn-link user-nav_link'"
                                           " and text()='Settings']")

        # Menu URLs
        self.garage_url = f"https://{login}:{passwd}@qauto.forstudy.space/panel/garage"
        self.expenses_url = f"https://{login}:{passwd}@qauto.forstudy.space/panel/expenses"
        self.instructions_url = f"https://{login}:{passwd}@qauto.forstudy.space/panel/instructions"

    def click_garage(self):
        """Click garage link in main header navigation"""
        garage_link = find(self.driver, *self.garage_link)
        click_button(self.driver, garage_link)

    def click_fuel_expenses(self):
        """Click fuel_expenses link in main header navigation"""
        f_expenses_link = find(self.driver, *self.fuel_expenses_link)
        click_button(self.driver, f_expenses_link)

    def click_instructions(self):
        """Click fuel_instructions link in main header navigation"""
        f_instructions_link = find(self.driver, *self.instructions_link)
        click_button(self.driver, f_instructions_link)

    def open_user_profile_menu(self):
        """Open Profile drop-down menu"""
        menu_button = find(self.driver, *self.profile_button)
        click_button(self.driver, menu_button)

    def click_logout(self):
        """CLick logout button in side-bar menu"""
        logout_button = find(self.driver, *self.logout_button)
        click_button(self.driver, logout_button)


class AddCarFrame(GaragePage):

    def __init__(self, driver):
        super().__init__(driver)

        # Frame drop down selectors and input
        self.brand_select = (By.ID, "addCarBrand")
        self.model_select = (By.ID, "addCarModel")
        self.millage_input = (By.ID, "addCarMileage")

        # Frame car brands and models
        self.brand_bmw = (By.XPATH, "//select/option[text()='BMW']")
        self.model_bmw3 = (By.XPATH, "//select/option[text()='3']")

        # Frame buttons
        self.add_button = (By.XPATH, "//button[text()='Add']")

        # Info frames
        self.car_added_frame = (By.XPATH, "//p[text()='Car added']")

    def select_car_brand(self, brand):
        """Open car brand drop down selector and choose car brand in list"""

        brand_selector = find(self.driver, *self.brand_select)
        click_button(self.driver, brand_selector)

        car_brand = find(self.driver, *brand)
        click_button(self.driver, car_brand)

    def select_car_model(self, model):
        """Open car model drop down selector and choose model in list"""

        model_selector = find(self.driver, *self.model_select)
        click_button(self.driver, model_selector)

        car_model = find(self.driver, *model)
        click_button(self.driver, car_model)

    def set_millage(self, millage):
        """Enter values in millage input"""

        millage_input = find(self.driver, *self.millage_input)
        enter_text(self.driver, millage_input, millage)

    def click_add_car(self):
        """Click add car button in add car frame"""

        add_car_button = find(self.driver, *self.add_button)
        click_button(self.driver, add_car_button)

    def wait_for_car_added_frame(self):
        """Wait for successful added car frame"""

        wait_element_to_be_located(self.driver, self.car_added_frame)
