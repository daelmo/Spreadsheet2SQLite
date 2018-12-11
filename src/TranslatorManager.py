from src.translator.CellAnnotationsTableTranslator import CellAnnotationsTableTranslator
from src.translator.AnnotationRangeTableTranslator import AnnotationRangeTableTranslator


class TranslatorManager:
    cellAnnotationsTranslator = CellAnnotationsTableTranslator()
    annotationRangeTranslator = AnnotationRangeTableTranslator()

    translatorList = ( cellAnnotationsTranslator, annotationRangeTranslator)

    def __init__(self, dbconnector):
        self.dbconnector = dbconnector

    def generateCreateTableSQL(self):
        for translator in self.translatorList:
            sql = translator.generateCreateTableSQL()
            self.dbconnector.execute(sql)

    def generateInsertSQL(self, csv_data):
        for translator in self.translatorList:
            sqlList = translator.translate(csv_data)
            for sql in sqlList:
                self.dbconnector.execute(sql)

    def generateCleanupSQL(self):
        for translator in self.translatorList:
            sql = translator.generateCleanupSQL()
            self.dbconnector.execute(sql)
