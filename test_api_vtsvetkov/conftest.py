import pytest
import requests

from endpoints.endpoint import Endpoint
from endpoints.create_post import CreatePost
from endpoints.put_post import PutPost
from endpoints.patch_post import PatchPost
from endpoints.delete_post import DeletePost


@pytest.fixture()
def manipulate_post():
    body = {"name": "Apple MacBook Pro 16", "data": {"year": 2019, "price": 1849.99, "CPU model": "Intel Core i9",
                                                     "Hard disk size": "1 TB"}}
    response = requests.post(Endpoint.url, json=body)
    post_id = response.json()['id']
    yield post_id
    response = requests.delete(Endpoint.url + f'/{post_id}')


@pytest.fixture()
def create_post_endpoint():
    return CreatePost()


@pytest.fixture()
def put_post_endpoint():
    return PutPost()


@pytest.fixture()
def patch_post_endpoint():
    return PatchPost()


@pytest.fixture()
def delete_post_endpoint():
    return DeletePost()
