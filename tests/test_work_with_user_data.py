import httpx
import allure
import datetime
from jsonschema import validate

from core.contracts import CREATED_USER_SCHEME, UPDATED_USER_SCHEME

BASE_URL = "https://reqres.in/"
CREATE_USER = "api/users"
UPDATE_USER = "api/users/2"
DELETE_USER = "api/users/2"

@allure.suite('Создание нового пользователя')
@allure.title('CREATE_USER')
def test_create_new_user():
    body = {
        "name": "morpheus",
        "job": "leader"
    }
    with allure.step(f'Выполнен запрос по адресу {BASE_URL + CREATE_USER}'):
        responce = httpx.post(BASE_URL + CREATE_USER, json=body)
    with allure.step('Код ответа 201'):
        assert responce.status_code == 201

    responce_json = responce.json()
    creation_data = responce_json['createdAt'].replace('T', ' ')
    current_data = str(datetime.datetime.utcnow())

    validate(responce_json, CREATED_USER_SCHEME)
    with allure.step(f'Ответ содержит переданный параметр name - {responce_json['name']}'):
        assert responce_json['name'] == body['name']
    with allure.step(f'Ответ содержит переданный параметр job - {responce_json['job']}'):
        assert responce_json['job'] == body['job']
    with allure.step(f'Ответ содержит параметр createdAt с текущей датой создания- {creation_data[0:16]}'):
        assert creation_data[0:16] == current_data[0:16]


@allure.suite('Обновление данных пользователя (put)')
@allure.title('UPDATE_USER with put')
def test_update_user_with_put():
    body = {
        "name": "morpheus",
        "job": "zion resident"
    }

    with allure.step(f'Выполнен запрос по адресу {BASE_URL+UPDATE_USER}'):
        responce = httpx.put(BASE_URL+UPDATE_USER, json=body)
    with allure.step('Код ответа 200'):
        assert responce.status_code == 200

    responce_json = responce.json()
    updated_data = responce_json['updatedAt'].replace('T', ' ')
    current_data = str(datetime.datetime.utcnow())

    validate(responce_json, UPDATED_USER_SCHEME)
    with allure.step(f'Ответ содержит переданный параметр name - {responce_json['name']}'):
        assert responce_json['name'] == body['name']
    with allure.step(f'Ответ содержит переданный параметр job - {responce_json['job']}'):
        assert responce_json['job'] == body['job']
    with allure.step(f'Ответ содержит параметр updatedAt с обновленной датой создания- {updated_data[0:16]}'):
        assert updated_data[0:16] == current_data[0:16]

@allure.suite('Обновление данных пользователя (patch)')
@allure.title('UPDATE_USER with patch')
def test_update_user_with_patch():
    body = {
        "name": "tom",
        "job": "zion resident"
    }

    with allure.step(f'Выполнен запрос по адресу {BASE_URL+UPDATE_USER}'):
        responce = httpx.patch(BASE_URL+UPDATE_USER, json=body)
    with allure.step('Код ответа 200'):
        assert responce.status_code == 200

    responce_json = responce.json()
    updated_data = responce_json['updatedAt'].replace('T', ' ')
    current_data = str(datetime.datetime.utcnow())

    validate(responce_json, UPDATED_USER_SCHEME)
    with allure.step(f'Ответ содержит переданный параметр name - {responce_json['name']}'):
        assert responce_json['name'] == body['name']
    with allure.step(f'Ответ содержит переданный параметр job - {responce_json['job']}'):
        assert responce_json['job'] == body['job']
    with allure.step(f'Ответ содержит параметр updatedAt с обновленной датой создания- {updated_data[0:16]}'):
        assert updated_data[0:16] == current_data[0:16]

@allure.suite('Обновление данных пользователя (patch без job)')
@allure.title('UPDATE_USER with patch')
def test_update_user_with_patch_without_job():
    body = {
        "name": "jerry"
    }
    with allure.step(f'Выполнен запрос по адресу {BASE_URL+UPDATE_USER}'):
        responce = httpx.patch(BASE_URL+UPDATE_USER, json=body)
    with allure.step('Код ответа 200'):
        assert responce.status_code == 200

    responce_json = responce.json()
    updated_data = responce_json['updatedAt'].replace('T', ' ')
    current_data = str(datetime.datetime.utcnow())

    validate(responce_json, UPDATED_USER_SCHEME)
    with allure.step(f'Ответ содержит переданный параметр name - {responce_json['name']}'):
        assert responce_json['name'] == body['name']
    with allure.step(f'Ответ содержит параметр updatedAt с обновленной датой создания- {updated_data[0:16]}'):
        assert updated_data[0:16] == current_data[0:16]


@allure.suite('Удаление пользователя')
@allure.title('DELETE_USER')
def test_delete_user():
    with allure.step(f'Выполнен запрос по адресу {BASE_URL+DELETE_USER}'):
        responce = httpx.delete(BASE_URL+DELETE_USER)
    with allure.step('Код ответа 204'):
        assert responce.status_code == 204
