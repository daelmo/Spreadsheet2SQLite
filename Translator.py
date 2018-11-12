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
        for row in df.iterrows():
            sql = 'INSERT INTO ' + self.tableName + ' ' + str(self.tableFormat) + ' VALUES ('
            for index in self.spreadsheetFormat:
                sql += self._escapeValues(row[1][index])
            sql = sql[:-1]
            sql += ');'
            sqlList.append(sql)
        return sqlList

    def _escapeValues(self, value):
        if isinstance(value, str):
            return '"' + str(value) + '",'
        elif value is False:
            return str(0) + ','
        elif value is True:
            return str(1) + ','
        else:
            return str(value) + ','

