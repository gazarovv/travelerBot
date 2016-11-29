# -*- coding: utf-8 -*-

import time

import telepot  # фреймворк для Telegramm


def greet(sender):
    """Handle /start message"""
    bot.sendMessage(sender.get('id'),  # отправление сообщения пользователю по id
                    'Hello, {0} {1}!'.format(sender.get('first_name'), sender.get('last_name')))


def vk(sender):
    """Handle /vk message"""
    bot.sendMessage(sender.get('id'),
                    'vk() function connected!')


def unknown(sender, command):
    """Handle unknown message"""
    bot.sendMessage(sender.get('id'),
                    'Unknown command: {}!'.format(command))


token = '266806768:AAFSxlmCQR3mAkgTteW10lm6vo0-Dtu0uFU'  # токен, полученный при регстрации
offset = int(open('offset.txt').read())  # читаем оффсет из файла
bot = telepot.Bot(token)


while True:
    if bot.getUpdates(offset + 1):  # получаем новые обновления с оффсетом + 1
        offset = int(open('offset.txt').read())  # читаем оффсет из файла
        open('offset.txt', 'w').write(str(offset + 1))  # при этом предыдущие соощбщения удаляются
        offset = int(open('offset.txt').read())  # читаем оффсет из файла
        update = bot.getUpdates(offset)[0]  # возвращает первую запись dict с вложенными list
        message = update.get('message')
        command = message.get('text')
        sender = message.get('from')

        # print("{0} \n {1} \n".format(update, command))

        # Парсинг команда бота
        if command == 'hi' or command == 'hello':
            greet(sender)
        elif command == 'vk':
            vk(sender)
        else:
            unknown(sender, command)

    else:
        pass
        # print('no updates')  # ожидание в секундах
    time.sleep(5)
