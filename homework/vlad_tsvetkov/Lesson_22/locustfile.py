from locust import task, HttpUser, between
from random import randint

payload = {"name": "Apple MacBook Pro 16", "data": {"year": 2019, "price": randint(1000, 5000),
                                                    "CPU model": "Intel Core i9",
                                                    "Hard disk size": f"{randint(1, 5)} TB"}}


class Poke(HttpUser):
    wait_time = between(0.5, 3.0)
    id = None

    @task
    def on_start(self):
        response = self.client.get('/objects')
        assert response.status_code == 200
        self.id = self.client.post('/objects', json=payload).json()['id']

    @task(2)
    def post_a_post(self):
        response = self.client.post('/objects', json=payload)
        assert response.status_code == 200
        self.id = response.json()['id']

    @task
    def get_post(self):
        self.url = f'/objects?id={self.id}'
        response = self.client.get(self.url)
        assert response.status_code == 200

    @task
    def delete_post(self):
        self.url = f'/objects/{self.id}'
        response = self.client.delete(self.url)
        assert response.status_code == 200
