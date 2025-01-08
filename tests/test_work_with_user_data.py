import httpx
from jsonschema import validate

from core.contracts import CREATED_USER_SCHEME

BASE_URL = "https://reqres.in/"
CREATE_USER = "api/users"

def test_create_new_user():
    body = {
        "name": "morpheus",
        "job": "leader"
    }
    responce = httpx.post(BASE_URL+CREATE_USER, json=body)
    response_json = responce.json()

    assert responce.status_code == 201
    validate(response_json, CREATED_USER_SCHEME)

    assert response_json['name'] == body['name']
    assert response_json['job'] == body['job']