from endpoints.delete_endpoint import DeleteMeme


def delete_meme(get_token, id):
    DeleteMeme().delete_meme(get_token, id)
