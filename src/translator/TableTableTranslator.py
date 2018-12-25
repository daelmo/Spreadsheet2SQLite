import pandas as pd

from src.translator.Translator import Translator

class TableTableTranslator(Translator):

    def __init__(self):
        self.tableName = 'tables'
        self.tableFormat = ('file_name','sheet_name', 'sheet_index', 'table_name', 'table_address', 'first_column',
                            'first_row','last_column', 'last_row')

    def translate(self, csv_data):
        return self.generateInsertSQL(csv_data['table_annotations_enron'])

