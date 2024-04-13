import requests

from endpoints.base_endpoint import BaseEndpoint


class PostMeme(BaseEndpoint):
    rel_url = '/meme'
    meme_text = "Фыр"
    meme_url = 'https://i.pinimg.com/736x/7a/f0/04/7af004703ee797756ba58c0b186fdca9.jpg'
    meme_tags = ['cat', 'kinda pokerface']
    meme_info = {"colors": ["white", "black"], "context": "cat_face"}

    def post_meme(self, token):
        body = {"text": self.meme_text,
                "url": self.meme_url,
                "tags": self.meme_tags,
                "info": self.meme_info}
        self.response = requests.post(f'{self.host}{self.rel_url}', json=body, headers={'Authorization': token})
        return self.response

    def post_meme_no_token(self):
        body = {"text": self.meme_text,
                "url": self.meme_url,
                "tags": self.meme_tags,
                "info": self.meme_info}
        self.response = requests.post(f'{self.host}{self.rel_url}', json=body)

    def post_meme_empty_body(self, token):
        body = {"text": "",
                "url": "",
                "tags": [""],
                "info": {}}
        self.response = requests.post(f'{self.host}{self.rel_url}', json=body, headers={'Authorization': token})

    def post_meme_no_body(self, token):
        body = {}
        self.response = requests.post(f'{self.host}{self.rel_url}', json=body, headers={'Authorization': token})

    def check_meme_data(self):
        json = self.response.json()
        assert json['text'] == self.meme_text
        assert json['url'] == self.meme_url
        assert json['tags'] == self.meme_tags
        assert json['info'] == self.meme_info
