from Sheet2TableTranslator import Sheet2TableTranslator
from Translator import Translator


class Workbook2SQLTranslator(Translator):
    sheet2TableTranslator = Sheet2TableTranslator()

    def createTables(self):
        sql = self.sheet2TableTranslator.createTables()
        return sql

    def translate(self,  sheet):
        sql = self.sheet2TableTranslator.translate(sheet)
        return sql

    def cleanup(self):
        sql = self.sheet2TableTranslator.cleanup()
        return sql
