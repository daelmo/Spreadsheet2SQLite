import pandas as pd

from src.translator.Translator import Translator

class RowHeightTableTranslator(Translator):

    def __init__(self):
        self.tableName = 'row_heights'
        self.tableFormat = ('file_name','sheet_name','sheet_index','row_index','row_height','is_hidden','is_empty')

    def translate(self, csv_data):
        return self.generateInsertSQL(csv_data['row_heights_enron'])

