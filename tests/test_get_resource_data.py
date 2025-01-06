import httpx
import allure
from jsonschema import validate
from core.contracts import RESOURCE_DATA_SCHEME

BASE_URL = "https://reqres.in/"
LIST_RESOURCE = "api/unknown"
SINGLE_RESOURCE = "api/unknown/2"
NOT_FOUND_RESOURCE = "api/unknown/23"

HEX = "#"
PANTONE = "-"

@allure.suite('Запрос на список Resource')
@allure.title('List <resource>')
def test_list_resource():
    with allure.step(f'Запрос по адресу:{BASE_URL + LIST_RESOURCE}'):
        response = httpx.get(BASE_URL + LIST_RESOURCE)

    with allure.step('Код ответа: 200'):
        assert response.status_code == 200
    data = response.json()['data']

    for item in data:
        with allure.step('Элемент списка'):
            validate(item, RESOURCE_DATA_SCHEME)
            with allure.step(f'Цвет color начинается с символа {HEX}'):
                assert item['color'].startswith(HEX)
            with allure.step(f'Pantone значение содержит символ {PANTONE}'):
                assert PANTONE in item['pantone_value']

@allure.suite('Запрос на один Resource')
@allure.title('Single <resource>')
def test_single_resource():
    with allure.step(f'Запрос по адресу:{BASE_URL + SINGLE_RESOURCE}'):
        response = httpx.get(BASE_URL + SINGLE_RESOURCE)

    with allure.step('Status code 200'):
        assert response.status_code == 200
    data = response.json()['data']

    with allure.step(f'Цвет color начинается с символа {HEX}'):
        assert data['color'].startswith(HEX)
    with allure.step(f'Pantone значение содержит символ {PANTONE}'):
        assert PANTONE in data['pantone_value']


@allure.suite('Запрос на несуществующий Resource')
@allure.title('Not found <resource>')
def test_not_found_resource():
    with allure.step(f'Запрос по адресу:{BASE_URL + NOT_FOUND_RESOURCE}'):
        response = httpx.get(BASE_URL + NOT_FOUND_RESOURCE)

    with allure.step('Status code 404'):
        assert response.status_code == 404

