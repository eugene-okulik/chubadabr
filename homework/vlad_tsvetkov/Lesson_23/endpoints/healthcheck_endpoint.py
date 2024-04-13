import requests

from endpoints.base_endpoint import BaseEndpoint


class HealthCheckTests(BaseEndpoint):
    rel_url = '/authorize'

    def token_healthcheck(self, token):
        self.response = requests.get(f'{self.host}{self.rel_url}/{token}')
        return self.response.text

    def token_not_exist(self, token):
        self.response = requests.get(f'{self.host}{self.rel_url}/{token} + "asdfg"')

    def token_not_given(self):
        self.response = requests.get(f'{self.host}{self.rel_url}')
