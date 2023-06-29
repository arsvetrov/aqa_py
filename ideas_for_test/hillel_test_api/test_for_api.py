from hillel_api import *
import pytest
global s

@pytest.fixture()
def give_exsist_user():

    user_data = {
        "name": "John",
        "lastName": "Dou",
        "email": "qam2906@2023test.com",
        "password": "Qam2608venv#",
        "repeatPassword": "Qam2608venv#"
        }
    # create user
    r = auth.signup(s, user_data)
    user_data = {
        "email": "qam2906@2023test.com",
        "password": "Qam2608venv#",
        "remember": True
        }
    # login
    r = auth.signin(s, user_data)
    headers = {"Cookie": r.headers.get('Set-Cookie'),
               'ETag': r.headers.get('ETag'),
               "Host": "qauto.forstudy.space",
               "Origin": "https://qauto.forstudy.space",
               "Referer": "https://qauto.forstudy.space/panel/settings"
               }
    # s.headers.update(headers)
    print("curr headers ", s.headers)
    print("cookie", s.cookies)
    r_json = after_processsing(r)
    print("before  test", r_json)
    yield
    #del user
    r = users.users(s)
    print("after  test", s.headers)
    print("cookie", s.cookies)
    print("after  test", r.json())


# def test_sigin_negative():

#     user_data_negative = {
#     "email": "qam@2022test.com",
#     "password": "Qam2",
#     "remember": False
#     }
#     r = auth.signin(s, user_data_negative)
#     r_json = after_processsing(r)
#     assert r.status_code == 400, "Wrong status code"
#     assert r_json["status"] == "error", "Key 'status' is not error"


# def test_logout():

#     r = auth.logout(s)
#     r_json = after_processsing(r)
#     assert r.status_code == 200, "Wrong status code"
#     assert r_json["status"] == "ok", "Key 'status' is not ok"

def test_get_user_data(give_exsist_user):

    r = users.current(s)
    r_json = after_processsing(r)
    assert False, r_json
