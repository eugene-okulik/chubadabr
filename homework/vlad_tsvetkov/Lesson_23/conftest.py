import pytest
import os

from endpoints.base_endpoint import BaseEndpoint
from endpoints.auth_endpoint import AuthTests
from endpoints.healthcheck_endpoint import HealthCheckTests
from endpoints.all_memes_endpoint import AllMemes
from endpoints.get_meme_endpoint import GetMeme
from endpoints.post_endpoint import PostMeme
from endpoints.put_endpoint import PutMeme
from endpoints.delete_endpoint import DeleteMeme
from dotenv import load_dotenv


@pytest.fixture()
def authorization_endpoint():
    return AuthTests()


@pytest.fixture()
def token_check():
    return HealthCheckTests()


@pytest.fixture()
def all_memes_endpoint():
    return AllMemes()


@pytest.fixture()
def one_meme_endpoint():
    return GetMeme()


@pytest.fixture()
def post_meme_endpoint():
    return PostMeme()


@pytest.fixture()
def put_meme_endpoint():
    return PutMeme()


@pytest.fixture()
def delete_meme_endpoint():
    return DeleteMeme()


@pytest.fixture()
def get_token():
    load_dotenv()
    if "TOKEN" in os.environ:
        token = os.environ['TOKEN']
        if HealthCheckTests().token_healthcheck(token) == BaseEndpoint.valid_text:
            return token
        else:
            os.environ['TOKEN'] = AuthTests().auth_get_token()
            return os.environ['TOKEN']
    else:
        os.environ['TOKEN'] = AuthTests().auth_get_token()
        return os.environ['TOKEN']


@pytest.fixture()
def get_one_meme():
    return AllMemes().get_random_meme_id(AuthTests().auth_get_token())


# Для метода удаления
@pytest.fixture()
def create_meme(get_token):
    response = PostMeme().post_meme(get_token)
    yield response.json()['id']


# Для метода редактирования
@pytest.fixture()
def create_and_delete_meme(get_token):
    response = PostMeme().post_meme(get_token)
    id = response.json()['id']
    yield id
    DeleteMeme().delete_meme(get_token, id)


# Для метода создания
# @pytest.fixture()
# def delete_meme():
#     yield

#     def _delete_meme(result):
#         return _delete_meme()
