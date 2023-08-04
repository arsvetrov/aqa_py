from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from lession_10 import my_logger as l
from pathlib import Path
import datetime


def take_screenshot(driver, file_prefix='screenshot'):
    """Makes screenshot with current date"""
    current_date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    file_name = f"{file_prefix}_{current_date}.png"
    folder_path = Path(__file__).parent / "screens"
    driver.save_screenshot(folder_path/file_name)


def find(driver, *elements):
    """Finds and processing a element"""
    try:
        element = driver.find_element(*elements)
        if element.is_displayed():
            return element
        else:
            l.logger.warning(f"\nElement: {elements} found but not displayed")
            return
    except (TimeoutException, NoSuchElementException):
        l.logger.error(f'\nElement: {elements} not found')
        take_screenshot(driver)


def click_button(driver, button):
    """Processing and clicks on elements"""

    button = WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable(button))
    try:
        button.click()
    except Exception as e:
        l.logger.error(f"\nElement: {button} is not clickable. Reason: {e}")


def enter_text(driver, field_input, text):
    """Processing input field and enter text in it"""
    try:
        field_input.clear()
        field_input.send_keys(text)
    except Exception as e:
        l.logger.error(f"\nText wasn't entered in input: {field_input}. Reason: {e}")
        take_screenshot(driver)


def wait_element_to_be_located(driver, element, timeout=10):
    """Processing wait element until it become visible"""
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(element))
    except Exception as e:
        l.logger.error(f"\nElement: {element} is not located. Reason: {e}")
        take_screenshot(driver)
