from Translator import Translator

class ToAnnotationTableTranslator(Translator):

    def __init__(self):
        self.tableName = 'annotations'
        self.tableFormat = ('sheet_id', 'sheet_name', 'annotation_label', 'table_id', 'total_cell_count', 'empty_cell_count', 'constant_cell_count', 'formula_cell_count',
                            'has_merged_cells', 'row_count', 'column_count', 'file_id', 'range_start', 'range_end')


    def translate(self, sheetdfs, fileID):
        self.spreadsheetFormat = ['Sheet.Index', 'Sheet.Name', 'Annotation.Label', 'Annotation.Name', 'TotalCells', 'EmptyCells', 'ConstantCells', 'FormulaCells',
                                  'HasMergedCells', 'Rows', 'Columns']
        sheetEntries = sheetdfs['Range_Annotations_Data'][self.spreadsheetFormat]
        sheetEntries = self._removeAllTableEntries(sheetEntries)
        sheetEntries = self._appendFileIDToDF(sheetEntries, fileID)
        sheetEntries = self._appendStartEndRangeToDF(sheetdfs, sheetEntries)
        return self.generateInsertSQL(sheetEntries)

    def _appendFileIDToDF(self, df, value):
        columnName = 'File.ID'
        df[columnName] = value
        self.spreadsheetFormat.append(columnName)
        return df

    def _appendStartEndRangeToDF(self, full_df, df):
        rangeEntries = full_df['Range_Annotations_Data']['Annotation.Range']
        rangeStartEntries = rangeEntries.apply(lambda x: (x.split(':')[0]).replace('$', ''))
        rangeEndEntries = rangeEntries.apply(lambda x: (x.split(':')[-1]).replace('$', ''))
        df['Range.Start'] = rangeStartEntries
        df['Range.End'] = rangeEndEntries
        self.spreadsheetFormat.append('Range.Start')
        self.spreadsheetFormat.append('Range.End')
        return df

    def _removeAllTableEntries(self, df):
        return df[df['Annotation.Label'] != 'Table']