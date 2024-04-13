import requests

from endpoints.base_endpoint import BaseEndpoint


class AuthTests(BaseEndpoint):
    rel_url = '/authorize'

    def auth_get_token(self):
        self.response = requests.post(f'{self.host}{self.rel_url}', json={"name": f"{self.nickname}"})
        self.token = self.response.json()['token']
        return self.token

    def auth_wrong_json(self):
        self.response = requests.post(f'{self.host}{self.rel_url}', json={"name": False})

    def auth_no_payload(self):
        self.response = requests.post(f'{self.host}{self.rel_url}')

    def auth_empty_name(self):
        self.response = requests.post(f'{self.host}{self.rel_url}', json={"name": ""})
