from Sheet2TableTranslator import Sheet2TableTranslator


class File2SQLManager():
    sheet2TableTranslator = Sheet2TableTranslator()
    _nextAvailableFileId = -1

    def __init__(self, dbconnector):
        self.dbconnector = dbconnector

    def generateCreateTableSQL(self):
        sql = self.sheet2TableTranslator.generateCreateTableSQL()
        self.dbconnector.execute(sql)

    def generateInsertSQL(self, sheet):
        self.incrementFileID()
        sqlList = self.sheet2TableTranslator.translate(sheet, self.getCurrentFileID())
        for sql in sqlList:
            self.dbconnector.execute(sql)

    def generateCleanupSQL(self):
        sql = self.sheet2TableTranslator.generateCleanupSQL()
        self.dbconnector.execute(sql)

    def getCurrentFileID(self):
        return self._nextAvailableFileId

    def incrementFileID(self):
        self._nextAvailableFileId += 1
