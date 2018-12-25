from src.translator.CellAnnotationsTableTranslator import CellAnnotationsTableTranslator
from src.translator.AnnotationRangeTableTranslator import AnnotationRangeTableTranslator
from src.translator.RowHeightTableTranslator import RowHeightTableTranslator
from src.translator.ColumnWidthTableTranslator import ColumnWidthTableTranslator
from src.translator.TableTableTranslator import TableTableTranslator


class TranslatorManager:
    cellAnnotationsTranslator = CellAnnotationsTableTranslator()
    annotationRangeTranslator = AnnotationRangeTableTranslator()
    heightTableTranslator = RowHeightTableTranslator()
    widthTableTranslator = ColumnWidthTableTranslator()
    tableTableTranslator = TableTableTranslator()

    translatorList = (cellAnnotationsTranslator, annotationRangeTranslator, heightTableTranslator, widthTableTranslator,
                      tableTableTranslator)

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
