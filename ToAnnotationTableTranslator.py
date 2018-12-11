from Translator import Translator

class ToAnnotationTableTranslator(Translator):

    def __init__(self):
        self.tableName = 'annotations_area'
        self.tableFormat = ('file_name','sheet_name','sheet_index','table_name','cell_address','first_column','first_row','last_column','last_row','cell_label','cell_type','cell_style','cell_font','is_merged','is_hidden')


    def translate(self, csv_data):
        return self.generateInsertSQL(csv_data['annotated_area_per_file'])

