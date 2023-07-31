from garage_page import Navigation
from elem_processing import find
import pytest


@pytest.mark.positive
def test_header_menu_garage(logged_user, driver):
    """Test click garage link"""

    navigation = Navigation(driver)
    navigation.click_garage()

    assert driver.current_url == navigation.garage_url
    assert "Garage" in driver.page_source
    assert "Add car" in driver.page_source


@pytest.mark.positive
def test_header_fuel_expenses(logged_user, driver):
    """Test click fuel expenses link"""

    navigation = Navigation(driver)
    navigation.click_fuel_expenses()

    assert driver.current_url == navigation.expenses_url
    assert "Fuel expenses" in driver.page_source
    assert "Add an expense" in driver.page_source


@pytest.mark.positive
def test_header_fuel_instructions(logged_user, driver):
    """Test click fuel instructions link"""

    navigation = Navigation(driver)
    navigation.click_instructions()

    assert driver.current_url == navigation.instructions_url
    assert "Instructions" in driver.page_source
    assert "Search" in driver.page_source


@pytest.mark.positive
def test_user_profile_menu(logged_user, driver):
    """Test opens user drop down menu then verify that
    needed elements are enabled"""

    navigation = Navigation(driver)
    navigation.open_user_profile_menu()

    garage = find(driver, *navigation.garage_link_drop)
    profile = find(driver, *navigation.profile_link_drop)
    fuel_expenses = find(driver, *navigation.fuel_expenses_link_drop)
    instructions = find(driver, *navigation.instructions_link_drop)
    settings = find(driver, *navigation.settings_link_drop)
    logout = find(driver, *navigation.logout_link_drop)

    assert garage.is_enabled()
    assert profile.is_enabled()
    assert fuel_expenses.is_enabled()
    assert instructions.is_enabled()
    assert settings.is_enabled()
    assert logout.is_enabled()
