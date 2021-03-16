import pytest

from delidog.models import Chat


@pytest.fixture
def chat():
    return Chat.get_chat(123)


def test_get_chat():
    chat = Chat.get_chat(123)

    assert isinstance(chat, Chat)
    assert chat.id == 123


def test_get_token():
    token = Chat.get_token(123)

    assert isinstance(token, str)
    assert len(token) == 32


def test_get_chat_by_token(chat):
    obj = Chat.get_chat_by_token(chat.token)
    
    assert chat == obj
