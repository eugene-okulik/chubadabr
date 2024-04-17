import requests

from endpoints.base_endpoint import BaseEndpoint
from random import choice


class AllMemes(BaseEndpoint):
    rel_url = '/meme'

    def get_all_memes(self, token):
        self.response = requests.get(f"{self.host}{self.rel_url}", headers={'Authorization': token})
        return self.response

    def get_all_memes_no_token(self):
        self.response = requests.get(f"{self.host}{self.rel_url}")

    def get_random_meme_id(self, token):
        self.response = self.get_all_memes(token)
        self.json = self.response.json()['data']
        self.meme_ids = [el['id'] for el in self.json]
        return choice(self.meme_ids)
