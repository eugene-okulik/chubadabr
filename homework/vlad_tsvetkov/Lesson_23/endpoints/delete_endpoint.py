import requests

from endpoints.base_endpoint import BaseEndpoint


class DeleteMeme(BaseEndpoint):
    rel_url = '/meme/'
    url = BaseEndpoint.host + rel_url

    def delete_meme(self, token, meme_id):
        self.response = requests.delete(f'{self.url}{meme_id}', headers={'Authorization': token})
        return self.response

    def delete_meme_no_token(self, meme_id):
        self.response = requests.delete(f'{self.url}{meme_id}')
        return self.response
