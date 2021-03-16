import peewee as pw
from delidog.db import BaseModel, db
from delidog.utils import get_token


def create_tables():
    with db:
        tables = [
            Chat,
        ]

        db.create_tables(tables)


class Chat(BaseModel):
    id = pw.BigIntegerField(
        primary_key=True,
        unique=True,
        index=True
    )
    token = pw.CharField(
        max_length=50,
        default=get_token,
        index=True
    )

    class Meta:
        table_name = 'chats'

    @classmethod
    def get_chat(cls, id: int):
        chat, _ = Chat.get_or_create(
            id=id,
            defaults=dict(
                id=id
            )
        )
        return chat

    @classmethod
    def get_token(cls, id: int) -> str:
        chat = Chat.get_chat(id=id)
        return chat.token

    @classmethod
    def get_chat_by_token(cls, token):
        return Chat.get(Chat.token == token)