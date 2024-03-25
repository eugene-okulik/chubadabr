import requests
import pytest
import allure

from data_for_tests import body

url = 'https://api.restful-api.dev/objects'


@pytest.fixture(scope="session")
def global_announce():
    print('\nStart testing')
    yield
    print('\nTesting complete')


@pytest.fixture()
def func_announce():
    print('\nbefore test')
    yield
    print('\nafter test')


@pytest.fixture()
def manipulate_post():
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post(url, json=body)
    assert response.status_code == 200
    post_id = response.json()['id']
    yield post_id
    response = requests.delete(url + f'/{post_id}')


@allure.suite("Обработка товара")
@allure.feature("Основной функционал товара")
@allure.title("Создание товара")
@pytest.mark.critical
@pytest.mark.parametrize('body', body)
def test_create_post(global_announce, func_announce, body):
    response = requests.post(url, json=body)
    with allure.step("Ожидаем получить 200й статус ответа на создание поста"):
        assert response.status_code == 200


@allure.suite("Обработка товара")
@allure.epic("Расширение функционала магазина")
@allure.feature("Дополнительный функционал товара")
@allure.title("Замена товара")
@pytest.mark.medium
def test_put_post(func_announce, manipulate_post):
    body = {
        "name": "Dell Vostro 7759",
        "data": {
            "year": 2018,
            "price": 777,
            "Hard disk size": "3 TB"
        }
    }
    response = requests.put(url + f'/{manipulate_post}', json=body)
    with allure.step("Ожидаем получить 200й статус на замену товара"):
        assert response.status_code == 200
    with allure.step("Ожидаем, что id товара в запросе и ответе совпадёт"):
        assert response.json()['id'] == manipulate_post


@allure.suite("Обработка товара")
@allure.epic("Расширение функционала магазина")
@allure.feature("Дополнительный функционал товара")
@allure.title("Редактирование товара")
def test_patch_post(func_announce, manipulate_post):
    body = {
        "data": {
            "year": 2025,
            "price": 100500,
            "Hard disk size": "3 TB"
        }
    }
    response = requests.patch(url + f'/{manipulate_post}', json=body)
    assert response.status_code == 200
    assert response.json()['id'] == manipulate_post


@allure.suite("Обработка товара")
@allure.tag('IN DEV')
@allure.feature("Основной функционал товара")
@allure.title("Удаление товара")
def test_delete_post(func_announce, manipulate_post):
    response = requests.delete(url + f'/{manipulate_post}')
    assert response.status_code == 200
