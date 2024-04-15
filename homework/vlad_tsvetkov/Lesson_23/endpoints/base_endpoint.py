class BaseEndpoint():
    host = "http://167.172.172.115:52355/"
    nickname = "Chuba"
    valid_text = f"Token is alive. Username is {nickname}"
    response = None
    meme_ids = []
    token = None
    obj_structure = ['id', 'info', 'tags', 'text', 'updated_by', 'url']
    meme_structure_len = 6

    def check_status_code(self, status_code):
        assert self.response.status_code == status_code

    def check_auth_text(self):
        assert self.response.status_code == 200
        assert self.response.text == self.valid_text

    def check_headers(self, header, value):
        assert self.response.headers[header] == value

    def check_header_not_empty(self, header):
        assert len(self.response.headers[header]) != 0

    def check_json_structure(self):
        assert len(self.response.json()) == self.meme_structure_len
        assert list(self.response.json().keys()) == self.obj_structure
