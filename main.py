import telebot
from telebot import types
import config
import CoronaAPI
import ORM_pony


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Hi! I'm bot that can send you information about the number of people infected with coronavirus.")
    bot.send_message(message.chat.id, 'Which country are you interested in?', reply_markup=menu_keyboard())
    bot.register_next_step_handler(message, send_number_infected)


def menu_keyboard():
    item1 = types.KeyboardButton("Russia")
    item2 = types.KeyboardButton("USA")
    item3 = types.KeyboardButton("Germany")
    item4 = types.KeyboardButton("France")
    item5 = types.KeyboardButton('Italy')
    item6 = types.KeyboardButton('Japan')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(item1, item2).add(item3, item4).add(
        item5, item6)
    return markup


@bot.message_handler(content_types=["text"])
def send_number_infected(message):
    try:
        a, b, c = CoronaAPI.qet_number_infected(message.text)
        bot.send_message(message.chat.id, f'In {a} {b} there were {c} infected')
        ORM_pony.add_log(message.from_user.username, a, b, c)
    except Exception:
        bot.send_message(message.chat.id, 'Uspokoisya ples')


if __name__ == '__main__':
    bot.infinity_polling()