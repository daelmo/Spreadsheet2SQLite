
#from Workbook2SQLTranslator import Workbook2SQLTranslator

class Sheet2TableTranslator():
    nextAvailableSheetId= 0
    tableName = 'sheet'

    def createTables(self):
        return 'CREATE TABLE ' + self.tableName + ' (sheet_id, sheet_name, file_id);'

    def translate(self, sheetdfs):
        sheetEntries = sheetdfs['Range_Annotations_Data'][['Sheet.Name', 'Sheet.Index']]
        uniqueSheetEntries = sheetEntries.drop_duplicates()
        print(uniqueSheetEntries)

        return ' '

    def cleanup(self):
        return 'DROP TABLE IF EXISTS ' + self.tableName + ';'