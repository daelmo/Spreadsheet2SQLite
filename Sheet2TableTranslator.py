
#from Workbook2SQLTranslator import Workbook2SQLTranslator

class Sheet2TableTranslator():
    def createTables(self):
        return 'CREATE TABLE sheet (sheet_id, sheet_name, file_id);'

    def translate(self, sheet):
        print(sheet.col_values( 0))
        return ' '

    def cleanup(self):
        return 'DROP TABLE IF EXISTS sheet;'