import pytest

from delidog.models import Chat
from delidog.utils import get_token


@pytest.fixture
def chat():
    return Chat.get_chat(123)


@pytest.fixture
def random_token():
    return get_token()


def test_get_chat():
    chat = Chat.get_chat(123)

    assert isinstance(chat, Chat)
    assert chat.id == 123


def test_set_token(random_token):
    Chat.set_token(123, random_token)
    chat = Chat.get_chat(123)

    assert chat.token == random_token


def test_get_token():
    token = Chat.get_token(123)

    assert isinstance(token, str)
    assert len(token) == 32


def test_get_chats_by_token(chat):
    obj = Chat.get_chats_by_token(chat.token)

    assert chat in obj
