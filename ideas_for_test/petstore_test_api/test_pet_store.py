from conftest import *


# Test 4
def test_get_user(create_user):
    r = User.get_user(s, "Name12312")
    r_json = json_validate(r)

    assert r.status_code == 200, "Status code is not 200 OK"
    assert r_json.get("username") == 'Name12312', "Incorrect user name received"
    assert r_json.get("email") == 'string12@gmail.com', "Incorrect user email received"
    assert r_json.get("password") == '123Abc_', "Incorrect user password received"


# Test 5
def test_get_pet(create_pet):
    r = Pet.get_pet(s, create_pet)
    r_json = json_validate(r)
    pet_id = str(r_json.get("id"))
    expected_category = {'id': 13,
                         'name': 'mad'}

    assert r.status_code == 200, "Status code is not 200 OK"
    assert create_pet == pet_id, "Pet id is invalid"
    assert r_json.get("name") == "doggie", "Pet name is invalid"
    assert r_json.get("category") == expected_category, "Pet category data is invalid"
