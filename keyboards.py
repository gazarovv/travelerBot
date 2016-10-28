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
second_msg_keyboard.row('Кафе', 'Ресторан', 'Музей')
second_msg_keyboard.row('Музей', 'Памятник')
second_msg_keyboard.row('Достопримечательность')
# Третье сообщение
third_msg = 'Если хотите найти что то еще повторно нажмите кнопку "Отправить локацию"'
