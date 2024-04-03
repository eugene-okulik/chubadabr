import allure
import requests

from endpoints.endpoint import Endpoint


class PatchPost(Endpoint):
    @allure.step('Editing post (patch method)')
    def patch_post(self, manipulate_post, payload):
        self.post_id = manipulate_post
        self.url += f'/{self.post_id}'
        self.response = requests.patch(self.url, json=payload)
        self.json = self.response.json()
