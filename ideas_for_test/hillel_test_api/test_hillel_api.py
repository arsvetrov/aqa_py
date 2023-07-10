from conftest import *


# Test 1
def test_get_settings(logged_user):
    """Positive get settings"""

    r = users.settings_get(s)
    r_json = after_processsing(r)
    expected_data = {
        'currency': 'usd',
        'distanceUnits': 'km'
    }
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not 'ok'"
    assert r_json["data"] == expected_data, "Data is not valid"


# Test 2
def test_get_cars(logged_user, new_cars):
    """Positive get cars list"""

    r = cars.cars_get(s)
    r_json = after_processsing(r)

    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not 'ok'"
    assert len(r_json["data"]) == 2, "Wrong car count received"
    assert r_json["data"][0]["id"] == new_cars[0], "Car 1 id is incorrect"
    assert r_json["data"][1]["id"] == new_cars[1], "Car 2 id is incorrect"


# Test 3
def test_signin(registered_user):
    """Negative Login with incorrect password"""

    user_data_negative = {
        "email": "apepsii@test.com",
        "password": "testam2608venv#",
        "remember": True
    }
    r = auth.signin(s, user_data_negative)
    r_json = after_processsing(r)
    assert r.status_code == 400, "Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not 'error'"
    assert r_json["message"] == 'Wrong email or password', 'Incorrect message received'
