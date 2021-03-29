import datetime
import peewee as pw
from delidog.db import BaseModel, db
from delidog.utils import get_token


def create_tables():
    with db:
        tables = [
            Chat,
            Message,
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
    def set_token(cls, id: int, token: str) -> str:
        chat = Chat.get_chat(id=id)
        chat.token = token
        chat.save()

        return chat

    @classmethod
    def get_token(cls, id: int) -> str:
        chat = Chat.get_chat(id=id)
        return chat.token

    @classmethod
    def get_chats_by_token(cls, token):
        return list(Chat.select().where(Chat.token == token))


class Message(BaseModel):
    created = pw.DateTimeField(default=datetime.datetime.now)
    chat = pw.ForeignKeyField(
        Chat,
        backref='messages',
        on_delete='CASCADE'
    )
    text = pw.TextField()
    disable_notification = pw.BooleanField(default=False)

    class Meta:
        table_name = 'messages'

    @ classmethod
    def add_message(cls,
                    chat: Chat,
                    text: str,
                    disable_notification: bool = False):

        message = Message(chat=chat,
                          text=text,
                          disable_notification=disable_notification
                          )
        message.save()
