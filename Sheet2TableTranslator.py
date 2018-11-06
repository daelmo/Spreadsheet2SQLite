
from Translator import Translator

class Sheet2TableTranslator(Translator):
    nextAvailableSheetId= 0
    tableName = 'sheet'
    tableFormat = ('sheet_id', 'sheet_name', 'file_id')
    spreadsheetFormat = ['Sheet.Index', 'Sheet.Name' ]

    def translate(self, sheetdfs):
        sheetEntries = sheetdfs['Range_Annotations_Data'][self.spreadsheetFormat]
        uniqueSheetEntries = sheetEntries.drop_duplicates()
        return self.generateInsertSQL(uniqueSheetEntries)
