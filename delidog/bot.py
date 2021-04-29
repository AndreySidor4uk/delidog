import telebot
from delidog import settings
from delidog.models import Chat, Message


bot = telebot.TeleBot(settings.BOT_TOKEN)


@bot.message_handler(commands=['start', ])
def _send_token(message):
    chat = Chat.get_chat(message.chat.id)
    send_message(chat, chat.token)


@bot.message_handler(commands=['set_token', ])
def _set_token(message):
    text_split = message.text.split()
    if len(text_split) != 2:
        return

    token = text_split[1]
    chat = Chat.set_token(message.chat.id, token)

    send_message(chat, 'New token {}'.format(chat.token))


def send_message(chat, text, disable_notification=False):
    bot.send_message(
        chat.id, text, disable_notification=disable_notification, timeout=5)
    Message.add_message(
        chat,
        text,
        disable_notification
    )


def polling():
    bot.polling()
