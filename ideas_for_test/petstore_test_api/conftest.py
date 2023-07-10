from petstore_api import *
import pytest
import logging

log = logging.getLogger(__name__)


@pytest.fixture()
def create_user():
    request_body = {
        "id": 0,
        "username": "Name12312",
        "firstName": "Firstname",
        "lastName": "lastName",
        "email": "string12@gmail.com",
        "password": "123Abc_",
        "phone": "1234",
        "userStatus": 0
    }

    # Create_user
    yield User.add_user(s, request_body)

    # Delete user
    User.delete_user(s, "Name12312")


@pytest.fixture()
def create_pet():
    request_body = {
        "id": 0,
        "category": {
            "id": 13,
            "name": "mad"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

    # Create pet
    r = Pet.add_pet(s, request_body)
    r_json = json_validate(r)
    try:
        pet_id = str(r_json.get("id"))
        yield pet_id

    # Delete pet
        Pet.delete_pet(s, pet_id)
    except TypeError:
        log.error("Invalid value received")
