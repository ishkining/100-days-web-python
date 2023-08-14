import os

from dotenv import load_dotenv
import telebot
import requests

load_dotenv()

token_telebot = os.environ.get('TELEBOT_API')
bot = telebot.TeleBot(token_telebot)


@bot.message_handler(commands=['start'])
def start(message):
    test_message = 'Hello'
    bot.send_message(message.from_user.id, test_message)


if __name__ == '__main__':
    bot.polling(none_stop=True)
