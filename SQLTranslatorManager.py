from ToTableTableTranslator import ToTableTableTranslator
from ToAnnotationTableTranslator import ToAnnotationTableTranslator


class SQLTranslatorManager():
    tableTableTranslator = ToTableTableTranslator()
    annotationTableTranslator = ToAnnotationTableTranslator()

    translatorList = (tableTableTranslator, annotationTableTranslator)

    _nextAvailableFileId = -1

    def __init__(self, dbconnector):
        self.dbconnector = dbconnector

    def generateCreateTableSQL(self):
        for translator in self.translatorList:
            sql = translator.generateCreateTableSQL()
            self.dbconnector.execute(sql)

    def generateInsertSQL(self, sheet):
        self._incrementFileID()
        for translator in self.translatorList:
            sqlList = translator.translate(sheet, self.getCurrentFileID())
            for sql in sqlList:
                self.dbconnector.execute(sql)


    def generateCleanupSQL(self):
        for translator in self.translatorList:
            sql = translator.generateCleanupSQL()
            self.dbconnector.execute(sql)

    def getCurrentFileID(self):
        return self._nextAvailableFileId

    def _incrementFileID(self):
        self._nextAvailableFileId += 1
