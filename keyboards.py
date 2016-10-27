from telebot import types

#First Keyboard
first_Msg = ' Добрый день! Я тут чтобы помочь вам правильно провести ваш досуг!\nЯ TravelerBot! Для начала ' \
        'работы вам необходимо нажеть кнопку "Отправить локацию"!'
first_Msg_Keyboard = types.ReplyKeyboardMarkup()
item_Btn_location = types.KeyboardButton('Отправить локацию')
item_Btn_location.request_location = True
first_Msg_Keyboard.row(item_Btn_location)
# Second Keyboard
second_Msg = 'А теперь выберите тип заведения:'
second_Msg_Keyboard = types.ReplyKeyboardMarkup()
second_Msg_Keyboard.row('Кафэ','Ресторан','Музей')
second_Msg_Keyboard.row('Музей','Памятник')
second_Msg_Keyboard.row('Достопримечательность')
# Третье сообщение
third_Msg = 'Если хотите найти что то еще повторно нажмите кнопку "Отправить локацию"'