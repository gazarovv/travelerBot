# -*- coding: utf-8 -*-

import config
import telebot
import keyboards
import urllib3
import json


class ApiRequest:
    def __init__(self, api_key=config.API_KEY):
        self.api_key = api_key  # Google API_KEY

    def get_nearest_places(self, latitude, longitude, place_type, radius):
        location = 'location={0},{1}'.format(latitude, longitude)
        radius = 'radius=' + str(radius)  # Радиус поиска (метры)
        types = 'types=' + place_type  # ДОБАВИТЬ ПРОВЕРКУ НА КОРРЕКТНОСТЬ ТИПА МЕСТА!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # name = 'name=cruise'  # ХЗ что это такое =(
        a_key = 'key=' + str(self.api_key)
        static_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'  # Статическая часть api-запроса
        dynamic_url = '{0}&{1}&{2}&{3}'.format(location, radius, types, a_key)  # генерируемая часть
        get_nearest_url = static_url + dynamic_url  # url для запроса
        response = http.request('GET', get_nearest_url).data.decode('utf-8')  # Получен JSON с кодировкой utf-8
        objects = json.loads(response)  # Распаковываем JSON
        return objects


class Position:
    """ Описывает позицию и предоставлет метод
        для нахождения ближайших мест по заданному типу """
    def __init__(self, longitude, latitude, radius=500):
        self.longitude = longitude  # Долгота
        self.latitude = latitude  # Широта
        self.radius = radius

    def get_nearest(self, place_type):
        places = {}  # Словарь, включающий в себя имя и координаты ближайших мест
        response = google_api.get_nearest_places(self.latitude, self.longitude, place_type, self.radius)
        if response.get('status') == 'OK':
            for obj in response.get('results'):
                places[obj.get('name')] = obj.get('geometry')['location']  # Наполнение словаря значениями
            return places
            # for place in places:
            #     print(place, places[place]['lat'], places[place]['lng'])
        else:
            return response.get('status')


bot = telebot.TeleBot(config.TOKEN)

http = urllib3.PoolManager()
urllib3.disable_warnings()

google_api = ApiRequest()

<<<<<<< HEAD

curr_position = Position(37.381278, 54.92008)
print(curr_position.get_nearest(config.types['Кафе']))
=======
curr_position = Position(37.381278, 54.92008)
print(curr_position.get_nearest('cafe'))
>>>>>>> master


@bot.message_handler(commands=['start', 'help'])
def print_help(message):
    bot.send_message(message.chat.id, keyboards.first_msg, reply_markup=keyboards.first_msg_keyboard)


@bot.message_handler(content_types=["location"])
def msg_location(message):
    curr_position.longitude = message.location.longitude  # Долгота
    curr_position.latitude = message.location.latitude    # Широта
    bot.send_message(message.chat.id, keyboards.second_msg, reply_markup=keyboards.second_msg_keyboard)
    # print('долгота - {0}, широта - {1}'.format(curr_position.longitude, curr_position.latitude))


@bot.message_handler(content_types="text")
def msg_type(message):  # Если не подходит под Type класса сделать вывод сообщения
<<<<<<< HEAD
    place_type = message.text
    if place_type in config.types:
        res = curr_position.get_nearest(config.types[place_type])  # Передаем тип места в качестве аргумента
=======
    if message.text == 'Кафе':
        res = curr_position.get_nearest('cafe')  # Передаем тип места в качестве аргумента
>>>>>>> master
        bot.send_message(message.chat.id, 'Список ближайших кафе: ')
        for place in res:
            bot.send_message(message.chat.id, place)
            bot.send_location(message.chat.id,
                              res[place]['lat'], res[place]['lng'], reply_markup=keyboards.first_msg_keyboard)
    else:
<<<<<<< HEAD
        bot.send_message(message.chat.id, 'Тип места задан не верно: {0}'.format(place_type))
=======
        bot.send_message(message.chat.id, 'Тип места задан не верно: {0}'.format(message.text))
>>>>>>> master

if __name__ == '__main__':
    bot.polling(none_stop=True)
