from src.translator.Translator import Translator

class AnnotationRangeTableTranslator(Translator):

    def __init__(self):
        self.tableName = 'annotations_area'
        self.tableFormat = ('file_name','sheet_name','annotated_area','first_column','first_row','last_column','last_row')

    def translate(self, csv_data):
        return self.generateInsertSQL(csv_data['annotated_area_per_file'])

