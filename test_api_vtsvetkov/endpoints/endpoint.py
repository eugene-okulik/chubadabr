import allure


class Endpoint:
    url = 'https://api.restful-api.dev/objects'
    response = None
    json = None
    headers = {'Content-type': 'application/json'}

    @allure.step('Check that response status code is correct')
    def check_response_status(self, status_code):
        assert self.response.status_code == status_code

    @allure.step('Check that its our post by post_id')
    def check_post_id(self):
        assert self.json['id'] == self.post_id
