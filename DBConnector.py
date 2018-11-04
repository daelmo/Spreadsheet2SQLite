import sqlite3
from sqlite3 import Error


class DBConnector:

    def __init__(self, filename):
        self.connection = self._createConnection(filename)

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

    def execute(self, sql):
        print(sql)
        cursor = self.connection.cursor()
        return cursor.execute(sql)


