import pandas as pd

from src.translator.Translator import Translator

class ColumnWidthTableTranslator(Translator):

    def __init__(self):
        self.tableName = 'column_widths'
        self.tableFormat = ('file_name','sheet_name','sheet_index','column_str','column_index','column_width','is_hidden','is_empty')

    def translate(self, csv_data):
        return self.generateInsertSQL(csv_data['column_widths_enron'])

