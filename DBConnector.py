import sqlite3
from sqlite3 import Error
from sqlite_functions import Point_is_in_Range


class DBConnector:

    def __init__(self, filename):
        self.connection = self._createConnection(filename)
        self.connection.create_function('Range_in', 3, Point_is_in_Range)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._closeConnection()

    def _createConnection(self, filename):
        try:
            return sqlite3.connect(filename)
        except Error as e:
            print(e)

    def _closeConnection(self):
        self.connection.close()

    def commit(self):
        self.connection.commit()

    def execute(self, sql):
        print(sql)
        cursor = self.connection.cursor()
        return cursor.execute(sql)


