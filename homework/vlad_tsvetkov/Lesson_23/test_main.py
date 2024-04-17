from service_funcs import delete_meme


def test_authorization_valid(authorization_endpoint):
    authorization_endpoint.auth_get_token()
    authorization_endpoint.check_status_code(200)


def test_authorization_empty_nickname(authorization_endpoint):
    authorization_endpoint.auth_empty_name()
    authorization_endpoint.check_status_code(200)  # сомнительно, но okay


def test_authorization_wrong_json(authorization_endpoint):
    authorization_endpoint.auth_wrong_json()
    authorization_endpoint.check_status_code(400)


def test_authorization_no_payload(authorization_endpoint):
    authorization_endpoint.auth_no_payload()
    authorization_endpoint.check_status_code(500)


def test_token_healthcheck(token_check, get_token):
    token_check.token_healthcheck(get_token)
    token_check.check_status_code(200)
    token_check.check_auth_text()


def test_token_not_exist(token_check, get_token):
    token_check.token_not_exist(get_token)
    token_check.check_status_code(404)


def test_token_not_sent(token_check):
    token_check.token_not_given()
    token_check.check_status_code(405)


def test_all_memes_endpoint(all_memes_endpoint, get_token):
    all_memes_endpoint.get_all_memes(get_token)
    all_memes_endpoint.check_status_code(200)
    all_memes_endpoint.check_headers('Content-Type', 'application/json')
    all_memes_endpoint.check_header_not_empty('Content-Length')


def test_all_memes_endpoint_no_token(all_memes_endpoint):
    all_memes_endpoint.get_all_memes_no_token()
    all_memes_endpoint.check_status_code(401)


def test_one_meme_endpoint(one_meme_endpoint, get_token, get_one_meme):
    one_meme_endpoint.one_meme(get_token, get_one_meme)
    one_meme_endpoint.check_status_code(200)
    one_meme_endpoint.check_json_structure()


def test_one_meme_endpoint_wrong_token(one_meme_endpoint, get_token, get_one_meme):
    one_meme_endpoint.one_meme_wrong_token(get_token, get_one_meme)
    one_meme_endpoint.check_status_code(401)


def test_one_meme_endpoint_no_token(one_meme_endpoint, get_one_meme):
    one_meme_endpoint.one_meme_no_token(get_one_meme)
    one_meme_endpoint.check_status_code(401)


def test_post_meme(post_meme_endpoint, get_token):
    meme_id = post_meme_endpoint.post_meme(get_token).json()['id']
    post_meme_endpoint.check_status_code(200)
    post_meme_endpoint.check_json_structure()
    post_meme_endpoint.check_meme_data()
    delete_meme(get_token, meme_id)


def test_post_meme_no_token(post_meme_endpoint):
    post_meme_endpoint.post_meme_no_token()
    post_meme_endpoint.check_status_code(401)


def test_post_meme_empty_body(post_meme_endpoint, get_token):
    post_meme_endpoint.post_meme_empty_body(get_token)
    post_meme_endpoint.check_status_code(200)  # ??))


def test_post_meme_no_body(post_meme_endpoint, get_token):
    post_meme_endpoint.post_meme_no_body(get_token)
    post_meme_endpoint.check_status_code(400)


def test_put_meme(put_meme_endpoint, get_token, create_and_delete_meme):
    put_meme_endpoint.edit_meme(get_token, create_and_delete_meme)
    put_meme_endpoint.check_status_code(200)


def test_put_meme_no_token(put_meme_endpoint, get_token, create_and_delete_meme):
    put_meme_endpoint.edit_meme_no_token(create_and_delete_meme)
    put_meme_endpoint.check_status_code(401)


def test_put_meme_empty_body(put_meme_endpoint, get_token, create_and_delete_meme):
    put_meme_endpoint.edit_meme_empty_body(get_token, create_and_delete_meme)
    put_meme_endpoint.check_status_code(200)


def test_put_meme_no_body(put_meme_endpoint, get_token, create_and_delete_meme):
    put_meme_endpoint.edit_meme_no_body(get_token, create_and_delete_meme)
    put_meme_endpoint.check_status_code(400)


def test_delete_meme(delete_meme_endpoint, create_meme, get_token):
    delete_meme_endpoint.delete_meme(get_token, create_meme)
    delete_meme_endpoint.check_status_code(200)


def test_delete_meme_no_token(delete_meme_endpoint, create_and_delete_meme):
    delete_meme_endpoint.delete_meme_no_token(create_and_delete_meme)
    delete_meme_endpoint.check_status_code(401)