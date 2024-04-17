import requests

from endpoints.auth_endpoint import BaseEndpoint


class GetMeme(BaseEndpoint):
    rel_url = '/meme/'
    url = BaseEndpoint.host + rel_url

    def one_meme(self, token, id):
        self.response = requests.get(f'{self.url}{id}', headers={'Authorization': token})

    def one_meme_wrong_token(self, token, id):
        self.response = requests.get(f'{self.url}{id}', headers={'Authorization': f'{token}+qwe123'})

    def one_meme_no_token(self, id):
        self.response = requests.get(f'{self.url}{id}')
