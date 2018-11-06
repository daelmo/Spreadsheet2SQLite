from Sheet2TableTranslator import Sheet2TableTranslator


class Workbook2SQLTranslator():
    sheet2TableTranslator = Sheet2TableTranslator()
    nextAvailableFileId = -1

    def generateCreateTableSQL(self):
        sql = self.sheet2TableTranslator.generateCreateTableSQL()
        return sql

    def translate(self,  sheet):

        sql = self.sheet2TableTranslator.translate(sheet)
        return sql

    def generateCleanupSQL(self):
        sql = self.sheet2TableTranslator.generateCleanupSQL()
        return sql

    def getCurrentFileID(self):
        return self.nextAvailableFileId

    def incrementFileID(self):
        self.nextAvailableFileId += 1
