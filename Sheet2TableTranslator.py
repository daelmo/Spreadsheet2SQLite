
from Translator import Translator

class Sheet2TableTranslator(Translator):
    nextAvailableSheetId= 0
    tableName = 'sheet'
    tableFormat = ('sheet_id', 'sheet_name', 'file_id')


    def translate(self, sheetdfs):
        sheetEntries = sheetdfs['Range_Annotations_Data'][['Sheet.Name', 'Sheet.Index']]
        uniqueSheetEntries = sheetEntries.drop_duplicates()
        print(uniqueSheetEntries)

        return ' '
