import httpx
from jsonschema import validate
from core.contracts import RESOURCE_DATA_SCHEME

BASE_URL = "https://reqres.in/"
LIST_RESOURCE = "api/unknown"
SINGLE_RESOURCE = "api/unknown/2"
NOT_FOUND_RESOURCE = "api/unknown/23"

HEX = "#"
PANTONE = "-"

def test_list_resource():
    response = httpx.get(BASE_URL + LIST_RESOURCE)
    assert response.status_code == 200
    data = response.json()['data']

    for item in data:
        validate(item, RESOURCE_DATA_SCHEME)
        assert item['color'].startswith(HEX)
        assert PANTONE in item['pantone_value']

def test_single_resource():
    response = httpx.get(BASE_URL + SINGLE_RESOURCE)
    assert response.status_code == 200
    data = response.json()['data']
    assert data['color'].startswith(HEX)
    assert PANTONE in data['pantone_value']


def test_not_found_resource():
    response = httpx.get(BASE_URL + NOT_FOUND_RESOURCE)
    assert response.status_code == 404

