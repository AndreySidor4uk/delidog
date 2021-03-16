import telebot
from delidog import settings
from delidog.models import Chat


bot = telebot.TeleBot(settings.BOT_TOKEN)


@bot.message_handler(commands=['start', ])
def _send_token(message):
    chat = Chat.get_chat(message.chat.id)
    send_message(chat, chat.token)


def send_message(chat, text, disable_notification=False):
    bot.send_message(
        chat.id, text, disable_notification=disable_notification)


def polling():
    bot.polling()
