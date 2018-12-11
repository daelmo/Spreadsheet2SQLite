import pandas as pd

class Translator:
    tableName = None
    tableFormat = None
    spreadsheetFormat = None

    def __init__(self):
        pass

    def translate(self, sheetdfs):
        pass

    def generateCleanupSQL(self):
        return 'DROP TABLE IF EXISTS ' + self.tableName + ';'

    def generateCreateTableSQL(self):
        return 'CREATE TABLE ' + self.tableName + ' ' + str(self.tableFormat) + ';'

    def generateInsertSQL(self, df):
        sqlList = []
        for index, row in df.iterrows():
            sql = 'INSERT INTO ' + self.tableName + ' ' + str(self.tableFormat)
            sql += ' VALUES ('
            for value in row:
                sql += self._escapeValues(value)
            sql = sql[:-1]
            sql += ');'
            sqlList.append(sql)
            print (sql)
            break
        return sqlList

    def _escapeValues(self, value):
        if value is '':
            return 'null,'
        elif isinstance(value, pd.Series):
            return '"' + value[0] + '",'
        elif value is False:
            return str(0) + ','
        elif value is True:
            return str(1) + ','
        elif isinstance(value, str):
            return '"' + value + '",'
        else:
            return str(value) + ','

