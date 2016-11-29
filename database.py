import sqlite3


class SQLighter:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def add(self, id, nickname):
        with self.connection:
            self.cursor.execute('INSERT INTO Users VALUES ({0}, {1});'.format(id, nickname))

    def selectall(self):
        """ Получаем все строки """
        with self.connection:
            return self.cursor.execute('SELECT * FROM Users').fetchall()

    def close(self):
        """ Закрываем текущее соединение с БД """
        self.connection.close()