import pytest
from hillel_api import *


@pytest.fixture()
def registered_user():
    # create user
    register_data = {
        "name": "Anatolii",
        "lastName": "Pepsi",
        "email": "apepsii@test.com",
        "password": "Qam2608venv#",
        "repeatPassword": "Qam2608venv#"
    }

    yield auth.signup(s, register_data)

    # delete user
    users.users(s)


@pytest.fixture()
def logged_user():
    # create user
    register_data = {
        "name": "Anatolii",
        "lastName": "Pepsi",
        "email": "apepsii@test.com",
        "password": "Qam2608venv#",
        "repeatPassword": "Qam2608venv#"
    }
    auth.signup(s, register_data)

    # login user
    login_data = {
        "email": "apepsii@test.com",
        "password": "Qam2608venv#",
        "remember": True
    }

    yield auth.signin(s, login_data)

    # delete user
    users.users(s)


@pytest.fixture()
def new_cars():

    car_data = {
        "carBrandId": 1,
        "carModelId": 1,
        "mileage": 122
    }

    # create two test cars
    r1 = cars.cars_post(s, car_data)
    r2 = cars.cars_post(s, car_data)
    r_json1 = after_processsing(r1)
    r_json2 = after_processsing(r2)

    # get car id's
    car1_id = r_json1["data"]["id"]
    car2_id = r_json2["data"]["id"]
    yield car1_id, car2_id

    # delete test cars
    cars.cars_id_delete(s, car1_id)
    cars.cars_id_delete(s, car2_id)
