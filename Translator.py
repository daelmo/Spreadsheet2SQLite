class Translator:
    tableName = None
    tableFormat = None
    spreadsheetFormat = None

    def __init__(self):
        pass

    def translate(self, sheetdfs):
        pass

    def cleanup(self):
        return 'DROP TABLE IF EXISTS ' + self.tableName + ';'

    def createTables(self):
        return 'CREATE TABLE ' + self.tableName + ' ' + str(self.tableFormat) + ';'

    def generateInsertSQL(self, df):
        sql = ''
        for row in df.iterrows():
            sql += 'INSERT INTO ' + self.tableName + ' ' + str(self.tableFormat) + ' VALUES ('
            for index in self.spreadsheetFormat:
                sql += self._escape(row[1][index])
            sql += '1'
            sql += ')'
        return sql

    def _escape(self, value):
        if isinstance(value, str):
            return '"' + str(value) + '",'
        else:
            return str(value) + ","