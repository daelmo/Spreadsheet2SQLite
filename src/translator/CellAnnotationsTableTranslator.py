import pandas as pd

from src.translator.Translator import Translator

class CellAnnotationsTableTranslator(Translator):

    def __init__(self):
        self.tableName = 'cell_annotations'
        self.tableFormat = ('file_name', 'sheet_name', 'sheet_index', 'table_name', 'cell_address', 'first_column', 'first_row', 'last_column', 'last_row', 'cell_label', 'cell_type', 'cell_style','cell_font', 'is_merged', 'is_hidden', 'is_empty')

    def translate(self, csv_data):
        df = csv_data['cell_annotations_enron']

        pd.read_excel(excel_file)

        # for each cell check in file check if empty
        return self.generateInsertSQL(df)

