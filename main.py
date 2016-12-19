# -*- coding: utf-8 -*-

import config
import telebot
import keyboards
import urllib3
import json
from database import SQLighter
import logging
import cherrypy


class WebhookServer(object):
    @cherrypy.expose
    def index(self):
        if 'content-length' in cherrypy.request.headers and \
                        'content-type' in cherrypy.request.headers and \
                        cherrypy.request.headers['content-type'] == 'application/json':
            length = int(cherrypy.request.headers['content-length'])
            json_string = cherrypy.request.body.read(length).decode("utf-8")
            update = telebot.types.Update.de_json(json_string)
            # Эта функция обеспечивает проверку входящего сообщения
            bot.process_new_updates([update])
            return ''
        else:
            raise cherrypy.HTTPError(403)

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
    def __init__(self, longitude, latitude, radius=400):
        self.longitude = longitude  # Долгота
        self.latitude = latitude  # Широта
        self.radius = radius

    def get_nearest(self, place_type):
        places = {}  # Словарь, включающий в себя имя и координаты ближайших мест
        response = google_api.get_nearest_places(self.latitude, self.longitude, place_type, self.radius)
        if response.get('status') == 'OK':
            for obj in response.get('results'):
                places[obj.get('name')] = obj.get('geometry')['location']
                # Наполнение словаря значениями
            return places
            # for place in places:
            #     print(place, places[place]['lat'], places[place]['lng'])
        else:
            return response.get('status')


bot = telebot.TeleBot(config.TOKEN)

http = urllib3.PoolManager()
urllib3.disable_warnings()
google_api = ApiRequest()
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('LOG.txt')
logger.addHandler(fh)
curr_position = Position(37.381278, 54.92008)


@bot.message_handler(commands=['start'])
def print_help(message):
    bot.send_message(message.chat.id, keyboards.first_msg, reply_markup=keyboards.first_msg_keyboard)
    db = SQLighter(config.DB_NAME)
    db.add(message.chat.id) # Не смог найти ник юзера
    print(message.chat.id, ' ', message.chat.first_name)
    print(db.selectall())
    db.close()


@bot.message_handler(commands=['help'])
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

    if message.text == 'Далее':
        bot.send_message(message.chat.id, keyboards.second_msg, reply_markup=keyboards.second_msg_keyboard2)
    if message.text == 'Назад':
        bot.send_message(message.chat.id, keyboards.second_msg, reply_markup=keyboards.second_msg_keyboard)
    if message.text == 'В начало':
        bot.send_message(message.chat.id, keyboards.first_msg, reply_markup=keyboards.first_msg_keyboard)
    if message.text != 'Далее' and message.text != 'В начало' and message.text != 'Назад':
        place_type = message.text
        if place_type in config.types:
            res = curr_position.get_nearest(config.types[place_type])  # Передаем тип места в качестве аргумента
            bot.send_message(message.chat.id, 'Список ближайших мест: ')
            try:
                for place in res:
                    bot.send_venue(message.chat.id,
                                res[place]['lat'], res[place]['lng'], place, ':',
                                   reply_markup=keyboards.first_msg_keyboard)
            except Exception:
                bot.send_message(message.chat.id, 'В радиусе {0}  метров нет таких мест'.format(800))
        else:
            bot.send_message(message.chat.id, 'Тип места задан не верно: {0}'.format(place_type))


"""if __name__ == '__main__':
    bot.polling(none_stop=True)"""


bot.remove_webhook()
 #Ставим заново вебхук
bot.set_webhook(url=config.WEBHOOK_URL_BASE + config.WEBHOOK_URL_PATH,
                certificate=open(config.WEBHOOK_SSL_CERT, 'r'))
cherrypy.config.update({
    'server.socket_host': config.WEBHOOK_LISTEN,
    'server.socket_port': config.WEBHOOK_PORT,
    'server.ssl_module': 'builtin',
    'server.ssl_certificate': config.WEBHOOK_SSL_CERT,
    'server.ssl_private_key': config.WEBHOOK_SSL_PRIV
})



cherrypy.quickstart(WebhookServer(), config.WEBHOOK_URL_PATH, {'/': {}})