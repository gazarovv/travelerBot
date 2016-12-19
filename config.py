# -*- coding: utf-8 -*-

DB_NAME = 'TravalerDB.db'
TOKEN = '280519474:AAHm-iwyzVNUp2owOfJymi5_wJBbe3a99jw'  # Telegram bot token GAZAROVV (TravelerBot)
API_KEY = 'AIzaSyAOvvTK4QZS5QSOrVqnDioh3FECde3ovr4'      # GOOGLE API KEY
types = {'Кафе': 'cafe', 'Бар': 'bar', 'Ресторан': 'restaurant', 'Клуб': 'night_club',
         'Еда': 'food', 'Музей': 'museum', 'Парк': 'park', 'Зоопарк': 'zoo',
         'Парковка': 'parking', 'Такси': 'taxi_stand', 'Метро': 'subway_station'}

WEBHOOK_HOST = '77.50.115.25'
WEBHOOK_PORT = 443  # 443, 80, 88 или 8443 (порт должен быть открыт!)
WEBHOOK_LISTEN = '127.0.0.1'  # На некоторых серверах придется указывать такой же IP, что и выше

WEBHOOK_SSL_CERT = './webhook_cert.pem'  # Путь к сертификату
WEBHOOK_SSL_PRIV = './webhook_pkey.pem'  # Путь к приватному ключу

WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % (TOKEN)



