import pytest
import allure

post_body = [
    {"name": "Apple MacBook Pro 16", "data": {"year": 2019, "price": 1849.99, "CPU model": "Intel Core i9",
                                              "Hard disk size": "1 TB"}},
    {"name": "Dell somethting", "data": {"year": 2018, "price": 1200, "CPU model": "Intel Core i5",
                                         "Hard disk size": "1 TB"}},
    {"name": "Lenovo Yoga", "data": {"year": 2021, "price": 1100, "CPU model": "Intel Core i3",
                                     "Hard disk size": "2 TB"}}
]


@allure.suite("Обработка товара")
@allure.feature("Основной функционал товара")
@allure.title("Создание товара")
@pytest.mark.critical
@pytest.mark.parametrize('body', post_body)
def test_creating_post(create_post_endpoint, body):
    create_post_endpoint.create_post(body)
    create_post_endpoint.check_response_status(200)


@allure.suite("Обработка товара")
@allure.epic("Расширение функционала магазина")
@allure.feature("Дополнительный функционал товара")
@allure.title("Замена товара")
@pytest.mark.medium
def test_put_post(put_post_endpoint, manipulate_post):
    body = {"name": "Dell Vostro 7759", "data": {"year": 2018, "price": 777, "Hard disk size": "3 TB"}}
    put_post_endpoint.replace_post(manipulate_post, payload=body)
    put_post_endpoint.check_post_id()
    put_post_endpoint.check_response_status(200)


@allure.suite("Обработка товара")
@allure.epic("Расширение функционала магазина")
@allure.feature("Дополнительный функционал товара")
@allure.title("Редактирование товара")
def test_patch_post(patch_post_endpoint, manipulate_post):
    body = {"data": {"year": 2025, "price": 100500, "Hard disk size": "3 TB"}}
    patch_post_endpoint.patch_post(manipulate_post, body)
    patch_post_endpoint.check_post_id()
    patch_post_endpoint.check_response_status(200)


@allure.suite("Обработка товара")
@allure.tag('IN DEV')
@allure.feature("Основной функционал товара")
@allure.title("Удаление товара")
def test_delete_post(delete_post_endpoint, manipulate_post):
    delete_post_endpoint.delete_post(manipulate_post)
    delete_post_endpoint.check_response_status(200)
