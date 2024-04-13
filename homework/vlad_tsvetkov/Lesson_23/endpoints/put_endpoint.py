import requests

from endpoints.base_endpoint import BaseEndpoint


class PutMeme(BaseEndpoint):
    rel_url = '/meme/'
    url = BaseEndpoint.host + rel_url
    meme_text = "Фыр_edited"
    meme_url = 'https://i.pinimg.com/1200x/ba/92/7f/ba927ff34cd961ce2c184d47e8ead9f6.jpg'
    meme_tags = ['cat', 'happy']
    meme_info = {"colors": ["striped", "white", "black", "brown"], "context": "happy_whiskers"}

    def edit_meme(self, token, meme_id):
        body = {"id": meme_id,
                "text": self.meme_text,
                "url": self.meme_url,
                "tags": self.meme_tags,
                "info": self.meme_info}
        self.response = requests.put(f'{self.url}{meme_id}', json=body, headers={'Authorization': token})

    def edit_meme_no_token(self, meme_id):
        body = {"id": meme_id,
                "text": self.meme_text,
                "url": self.meme_url,
                "tags": self.meme_tags,
                "info": self.meme_info}
        self.response = requests.put(f'{self.url}{meme_id}', json=body)

    def edit_meme_empty_body(self, token, meme_id):
        body = {"id": meme_id,
                "text": "",
                "url": "",
                "tags": [""],
                "info": {}}
        self.response = requests.put(f'{self.url}{meme_id}', json=body, headers={'Authorization': token})

    def edit_meme_no_body(self, token, meme_id):
        body = {}
        self.response = requests.put(f'{self.url}{meme_id}', json=body, headers={'Authorization': token})
