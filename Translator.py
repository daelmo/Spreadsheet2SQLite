class Translator:
    tableName = None

    def __init__(self):
        pass

    def translate(self):
        pass

    def cleanup(self):
        return 'DROP TABLE IF EXISTS ' + self.tableName + ';'

    def createTables(self):
        return 'CREATE TABLE ' + self.tableName + ' ' + str(self.tableFormat) + ';'

