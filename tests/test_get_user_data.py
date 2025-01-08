import httpx
import allure
from jsonschema import validate
from core.contracts import USER_DATA_SCHEME

BASE_URL = "https://reqres.in/"
LIST_USERS = "api/users?page=2"
SINGLE_USER = "api/users/2"
NOT_FOUND = "users/23"
EMAIL_ENDS = "reqres.in"
AVATAR_ENDS = "-image.jpg"

@allure.suite('Проверка api запросов')
@allure.title('Получен список юзеров')
def test_list_users():
    with allure.step(f'Выполнен запрос по адресу: {BASE_URL + LIST_USERS}'):
        response = httpx.get(BASE_URL + LIST_USERS)

    with allure.step('Код ответа: 200'):
        assert response.status_code == 200
    data = response.json()['data']

    for item in data:
        with allure.step(f'Элемент списка'):
            validate(item, USER_DATA_SCHEME)
            with allure.step(f'email оканчивается на {EMAIL_ENDS}'):
                assert item['email'].endswith(EMAIL_ENDS)
            with allure.step(f'наличие {item['id']} в {item['avatar']}'):
                assert str(item['id']) in item['avatar']
            with allure.step(f'{item['avatar']} содержит окончание {item['id']} +{AVATAR_ENDS}'):
                assert item['avatar'].endswith(str(item['id']) + AVATAR_ENDS)

@allure.suite('Запрос на одного юзера')
@allure.title('Single <user>')
def test_single_user():
    with allure.step(f' Выполнен запрос по адресу: {BASE_URL + SINGLE_USER}'):
        response = httpx.get(BASE_URL + SINGLE_USER)
    with allure.step('Status code 200'):
        assert response.status_code == 200
    data = response.json()['data']

    with allure.step(f'{data['email']} содержит окончание {EMAIL_ENDS}'):
        assert data['email'].endswith(EMAIL_ENDS)
    with allure.step(f'{data['avatar']} содержит окончание {str(data['id']) + AVATAR_ENDS}'):
        assert data['avatar'].endswith(str(data['id']) + AVATAR_ENDS)

@allure.suite('Запрос на несуществующий юзера')
@allure.title('Not found <user>')
def test_not_found_user():
    with allure.step(f' Выполнен запрос по адресу: {BASE_URL + NOT_FOUND}'):
        response = httpx.get(BASE_URL + NOT_FOUND)
    with allure.step('Status code 404'):
        assert response.status_code == 404


