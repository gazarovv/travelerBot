# -*- coding: utf-8 -*-

import config
import telebot
import keyboards

bot = telebot.TeleBot(config.token)


class Place:
    def __init__(self, name, lon, lat, type):
        self.name = name
        self.type = ['Кафэ', 'Ресторан', 'Фастфуд', 'Музей', 'Монумент', 'Древности']  # Доделать Класс
        self.lon = lon
        self.lat = lat
        self.rating = 0

    def __str__(self):
        return 'Name:{0} Type:{1} Rating:{2}'.format(self.name, self.type,self.rating)


@bot.message_handler(commands=['start', 'help'])
def print_help(message):
    bot.send_message(message.chat.id, keyboards.first_msg, reply_markup=keyboards.first_msg_keyboard)


@bot.message_handler(content_types=["location"])
def msg_location(message):
    bot.send_message(message.chat.id, message.location)  # Вывод коордианты {longitude, latitude}
    bot.send_message(message.chat.id, keyboards.second_msg, reply_markup=keyboards.second_msg_keyboard)
    # bot.send_message(message.chat.id, keyboards.third_Msg, reply_markup=keyboards.first_Msg_Keyboard)


@bot.message_handler(content_types="text")
def msg_type(message):  # Если не подходит под Type класса сделать вывод сообщения
    bot.send_message(message.chat.id, 'Тип: {0}'.format(message.text))


if __name__ == '__main__':
    bot.polling(none_stop=True)
