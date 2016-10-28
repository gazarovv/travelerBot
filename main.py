# -*- coding: utf-8 -*-

import config
import telebot
import keyboards
import urllib3
import json

bot = telebot.TeleBot(config.TOKEN)

http = urllib3.PoolManager()
urllib3.disable_warnings()


class Position:
    """ Описывает позицию и предоставлет метод
        для нахождения ближайших мест по заданному типу """
    def __init__(self, longitude, latitude, api_key=config.API_KEY):
        self.longitude = longitude  # Долгота
        self.latitude = latitude  # Широта
        self.api_key = api_key  # Google API_KEY

    def get_nearest(self, place_type):
        location = 'location={0},{1}'.format(self.latitude, self.longitude)
        radius = 'radius=' + str(500)  # Радиус поиска (размеронсть не ясна)
        types = 'types=' + place_type  # ДОБАВИТЬ ПРОВЕРКУ НА КОРРЕКТНОСТЬ ТИПА МЕСТА!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # name = 'name=cruise'  # ХЗ что это такое =(
        a_key = 'key=' + str(self.api_key)
        static_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'  # Статическая часть api-запроса
        dynamic_url = '{0}&{1}&{2}&{3}'.format(location, radius, types, a_key)  # генерируемая часть
        get_nearest_url = static_url + dynamic_url  # url для запроса
        response = http.request('GET', get_nearest_url).data.decode('utf-8')  # Получен JSON с кодировкой utf-8
        objects = json.loads(response)  # Распаковываем JSON
        places = {}  # Словарь, включающий в себя имя и координаты ближайших мест

        status = objects.get('status')
        if status == 'OK':
            for obj in objects.get('results'):
                places[obj.get('name')] = obj.get('geometry')['location']  # Наполнение словаря значениями
            return places
            # for place in places:
            #     print(place, places[place]['lat'], places[place]['lng'])
        else:
            return status

# curr_position = Position(37.381278, 54.92008)
# print(curr_position.get_nearest('cafe'))


@bot.message_handler(commands=['start', 'help'])
def print_help(message):
    bot.send_message(message.chat.id, keyboards.first_msg, reply_markup=keyboards.first_msg_keyboard)


@bot.message_handler(content_types=["location"])
def msg_location(message):
    curr_position.longitude = message.location.longitude  # Долгота
    curr_position.latitude = message.location.latitude    # Широта
    bot.send_message(message.chat.id, keyboards.second_msg, reply_markup=keyboards.second_msg_keyboard)


@bot.message_handler(content_types="text")
def msg_type(message):  # Если не подходит под Type класса сделать вывод сообщения
    if message.text == 'Кафе':
        res = curr_position.get_nearest('cafe')  # Передаем тип места в качестве аргумента
        bot.send_message(message.chat.id, 'Список ближайших кафе: ')
        for place in res:
            bot.send_message(message.chat.id, place)
            bot.send_location(message.chat.id,
                              res[place]['lat'], res[place]['lng'], reply_markup=keyboards.first_msg_keyboard)
    else:
        bot.send_message(message.chat.id, 'Тип места задан не верно: {0}'.format(message.text))

if __name__ == '__main__':
    bot.polling(none_stop=True)
