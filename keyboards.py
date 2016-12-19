# -*- coding: utf-8 -*-

from telebot import types

# First Keyboard
first_msg = 'Добрый день! Я тут чтобы помочь вам правильно провести ваш досуг!\nЯ TravelerBot! Для начала ' \
        'работы вам необходимо нажеть кнопку "Отправить локацию"!'
first_msg_keyboard = types.ReplyKeyboardMarkup()
item_btn_location = types.KeyboardButton('Отправить локацию')
item_btn_location.request_location = True
first_msg_keyboard.row(item_btn_location)
# Second Keyboard
second_msg = 'А теперь выберите тип заведения:'
second_msg_keyboard = types.ReplyKeyboardMarkup()
second_msg_keyboard.row('Кафе', 'Ресторан', 'Бар')
second_msg_keyboard.row('Клуб', 'Еда', 'Музей')
second_msg_keyboard.row('Далее', 'В начало')

second_msg_keyboard2 = types.ReplyKeyboardMarkup()
second_msg_keyboard2.row('Парк', 'Зоопарк', 'Такси')
second_msg_keyboard2.row('Метро', 'Парковка')
second_msg_keyboard2.row('Назад', 'В начало')
# Третье сообщение
third_msg = 'Если хотите найти что то еще повторно нажмите кнопку "Отправить локацию"'
