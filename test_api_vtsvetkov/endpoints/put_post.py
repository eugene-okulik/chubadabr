import allure
import requests

from endpoints.endpoint import Endpoint


class PutPost(Endpoint):
    @allure.step('Replacing post (put method)')
    def replace_post(self, manipulate_post, payload):
        self.post_id = manipulate_post
        self.url += f'/{self.post_id}'
        self.response = requests.put(self.url, json=payload)
        self.json = self.response.json()
