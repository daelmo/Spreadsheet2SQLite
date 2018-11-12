import pandas as pd

from Translator import Translator

class Sheet2TableTranslator(Translator):

    def __init__(self):
        self.tableName = 'sheet'
        self.tableFormat = ('sheet_id', 'sheet_name', 'file_id')

    def translate(self, sheetdfs, fileID):
        self.spreadsheetFormat = ['Sheet.Index', 'Sheet.Name']
        sheetEntries = sheetdfs['Range_Annotations_Data'][self.spreadsheetFormat]
        sheetEntries = self.appendColumnToDF(sheetEntries, 'File.ID', fileID)

        return self.generateInsertSQL(sheetEntries)
