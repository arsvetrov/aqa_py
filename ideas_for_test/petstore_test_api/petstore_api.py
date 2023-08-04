import requests

base_api_url = "https://petstore.swagger.io/v2"
s = requests.session()


class Pet:

    endpoint = "/pet/"

    def add_pet(s: requests.session, request_body: dict):
        return s.post(base_api_url + Pet.endpoint, json=request_body)

    def get_pet(s: requests.session, pet_id: str):
        return s.get(base_api_url + Pet.endpoint + pet_id)

    def update_pet(s: requests.session, request_body: dict):
        return s.put(base_api_url + Pet.endpoint, json=request_body)

    def delete_pet(s: requests.session, pet_id):
        return s.delete(base_api_url + Pet.endpoint + pet_id)


class User:

    endpoint = "/user/"

    def add_user(s: requests.session, request_body: dict):
        return s.post(base_api_url + User.endpoint, json=request_body)

    def get_user(s: requests.session, user_name: str):
        return s.get(base_api_url + User.endpoint + user_name)

    def delete_user(s: requests.session, user_name: str):
        return s.delete(base_api_url + User.endpoint + user_name)


def json_validate(r):
    try:
        return r.json()
    except Exception as e:
        return {}
