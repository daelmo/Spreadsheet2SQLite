import pandas as pd

from Translator import Translator

class ToTableTableTranslator(Translator):

    def __init__(self):
        self.tableName = 'tables'
        self.tableFormat = ('sheet_id', 'sheet_name', 'annotation_label', 'annotation_id', 'total_cell_count', 'empty_cell_count', 'constant_cell_count', 'formula_cell_count',
                            'has_merged_cells', 'row_count', 'column_count', 'file_id', 'file_name', 'table_id', 'range_start', 'range_end')

    def translate(self, sheetdfs, fileID, fileName):
        self.spreadsheetFormat = ['Sheet.Index', 'Sheet.Name', 'Annotation.Label', 'Annotation.Name', 'TotalCells', 'EmptyCells', 'ConstantCells', 'FormulaCells',
                                  'HasMergedCells', 'Rows', 'Columns']
        sheetEntries = sheetdfs['Range_Annotations_Data'][self.spreadsheetFormat]
        sheetEntries = self._removeAllNotTableEntries(sheetEntries)
        sheetEntries = self._appendFileIDToDF(sheetEntries, fileID)
        sheetEntries = self._appendFileNameToDF(sheetEntries, fileName)
        sheetEntries = self._appendTableIDToDF(sheetEntries)
        sheetEntries = self._appendStartEndRangeToDF(sheetdfs, sheetEntries)
        return self.generateInsertSQL(sheetEntries)

    def _appendFileIDToDF(self, df, value):
        columnName = 'File.ID'
        df[columnName] = value
        self.spreadsheetFormat.append(columnName)
        return df

    def _appendFileNameToDF(self, df, fileName):
        columnName = 'File.Name'
        df[columnName] = fileName
        self.spreadsheetFormat.append(columnName)
        return df

    def _removeAllNotTableEntries(self, df):
        return df[df['Annotation.Label'] == 'Table']

    def _removeAnnotationLabel(self, df, label):
        del df[label]
        return df

    def _appendTableIDToDF(self, df):
        df['Table.ID'] = list(range( df.shape[0]))
        self.spreadsheetFormat.append('Table.ID')
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
