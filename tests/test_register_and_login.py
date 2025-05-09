import json
import httpx
import pytest
from jsonschema import validate
from core.contracts import REGISTERED_USER_SCHEME, LOGGEDIN_USER_SCHEME

BASE_URL = "https://reqres.in/"
REGISTER_USER = "api/register"
LOGIN_USER = "api/login"

json_file_new_users_data = open('/Users/Anna/PycharmProjects/API_users/core/new_users_data.json')
json_file_user_data_only_email = open('/Users/Anna/PycharmProjects/API_users/core/user_data_only_email.json')

users_data = json.load(json_file_new_users_data)
user_data_only_email = json.load(json_file_user_data_only_email)

@pytest.mark.parametrize('users_data', users_data)
def test_successful_register(users_data):
    headers = {'Content-type': 'application/json'}
    response = httpx.post(BASE_URL+REGISTER_USER, json=users_data, headers=headers)
    assert response.status_code == 200

    validate(response.json(), REGISTERED_USER_SCHEME)

@pytest.mark.parametrize('user_data_only_email', user_data_only_email)
def test_unsuccessful_register(user_data_only_email):
    headers = {'Content-type': 'application/json'}
    response = httpx.post(BASE_URL + REGISTER_USER, json=user_data_only_email, headers=headers)
    assert response.status_code == 400

@pytest.mark.parametrize('users_data', users_data)
def test_successful_login(users_data):
    headers = {'Content-type': 'application/json'}
    response = httpx.post(BASE_URL+LOGIN_USER, json=users_data, headers=headers)
    assert response.status_code == 200

    validate(response.json(), LOGGEDIN_USER_SCHEME)

@pytest.mark.parametrize('user_data_only_email', user_data_only_email)
def test_unsuccessful_login(user_data_only_email):
    headers = {'Content-type': 'application/json'}
    response = httpx.post(BASE_URL+LOGIN_USER, json=user_data_only_email, headers=headers)
    assert response.status_code == 400


