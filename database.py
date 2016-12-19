import sqlite3


class SQLighter:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def add(self, id):
        with self.connection:
            try:
                self.cursor.execute('INSERT INTO Users VALUES ({0})'.format(id))
            except Exception:
                print('ID is not inique')

    def selectall(self):
        """ Получаем все строки """
        with self.connection:
            return self.cursor.execute('SELECT * FROM Users').fetchall()

    def close(self):
        """ Закрываем текущее соединение с БД """
        self.connection.close()
