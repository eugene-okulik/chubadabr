import allure
import requests

from endpoints.endpoint import Endpoint


class CreatePost(Endpoint):
    @allure.step('Creating post')
    def create_post(self, payload):
        self.response = requests.post(self.url, json=payload)
        self.json = self.response.json()
