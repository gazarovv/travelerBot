import config
import telebot
import keyboards

bot = telebot.TeleBot(config.token)

class Place:
    def __init__(self, Name, Lon, Lat, Type):
        self.Name = Name
        self.Type =['Кафэ', 'Ресторан','Фастфуд','Музей','Монумент','Древности'] #Доделать Класс
        self.Lon = Lon
        self.Lat = Lat
        self.Rating = 0

    def __str__(self):
        return 'Name:{0} Type:{1} Rating:{2}'.format(self.Name, self.Type,self.Rating)


@bot.message_handler(commands=['start', 'help'])
def printhelp(message):
    bot.send_message(message.chat.id, keyboards.first_Msg, reply_markup=keyboards.first_Msg_Keyboard)


@bot.message_handler(content_types=["location"])
def msgLocation(message):
    bot.send_message(message.chat.id, message.location)
    bot.send_message(message.chat.id, keyboards.second_Msg, reply_markup=keyboards.second_Msg_Keyboard)
   # bot.send_message(message.chat.id, keyboards.third_Msg, reply_markup=keyboards.first_Msg_Keyboard)


@bot.message_handler(content_types="text")
def msgType(message):
    bot.send_message(message.chat.id, 'Тип: {0}'.format(message.text)) #Если не подходит под Type класса сделать вывод сообщения


if __name__ == '__main__':
     bot.polling(none_stop=True)