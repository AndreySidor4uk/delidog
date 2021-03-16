import secrets


def get_token():
    return secrets.token_hex(16)
