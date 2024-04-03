import allure
import requests

from endpoints.endpoint import Endpoint


class DeletePost(Endpoint):
    @allure.step('Deleting post')
    def delete_post(self, manipulate_post):
        self.post_id = manipulate_post
        self.url += f'/{self.post_id}'
        self.response = requests.delete(self.url)
