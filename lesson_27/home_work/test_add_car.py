from garage_page import GaragePage
from garage_page import AddCarFrame
import pytest


@pytest.mark.positive()
def test_add_car(driver, logged_user):
    """Test add car with specific brand model and millage"""

    garage_page = GaragePage(driver)
    garage_page.click_add_car()

    add_car_form = AddCarFrame(driver)
    add_car_form.select_car_brand(add_car_form.brand_bmw)
    add_car_form.select_car_model(add_car_form.model_bmw3)
    add_car_form.set_millage("12000")
    add_car_form.click_add_car()

    add_car_form.wait_for_car_added_frame()

    assert driver.current_url == garage_page.url
    assert "Car added" in driver.page_source
    assert "BMW 3" in driver.page_source
    # Тут мала бути ще перевірка на 12000 міляжу але цього блоку немає в HTML за це відповідає якийсь application
    # https://aws3.link/TiikkE
