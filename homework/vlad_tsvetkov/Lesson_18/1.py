import requests

url = 'https://api.restful-api.dev/objects'


def create_post():
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
    post_id = response.json()['id']
    assert response.status_code == 200
    return post_id


def put_post():
    id = create_post()
    body = {
        "name": "Dell Vostro 7759",
        "data": {
            "year": 2018,
            "price": 777,
            "Hard disk size": "3 TB"
        }
    }
    response = requests.put(url + f'/{id}', json=body)
    assert response.status_code == 200
    assert response.json()['id'] == id


def patch_post():
    id = create_post()
    body = {
        "data": {
            "year": 2025,
            "price": 100500,
            "Hard disk size": "3 TB"
        }
    }
    response = requests.patch(url + f'/{id}', json=body)
    assert response.status_code == 200
    assert response.json()['id'] == id


def delete_post():
    id = create_post()
    response = requests.delete(url + f'/{id}')
    assert response.status_code == 200


create_post()
put_post()
patch_post()
delete_post()
print('Done')
