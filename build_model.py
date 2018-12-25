#!/usr/bin/python
import os
import pandas as pd
from src.DBConnector import DBConnector
from src.translator.TranslatorManager import TranslatorManager
from src.translator.CellAnnotationsTableTranslator import CellAnnotationsTableTranslator



DIRECTORY_PATH = './data/'

if __name__ == '__main__':

    with DBConnector('sqlite.db') as dbconnector:

        translatorManager = TranslatorManager(dbconnector)
        translatorManager.generateCleanupSQL()
        translatorManager.generateCreateTableSQL()

        print('Start reading files.')
        csv_data = {}
        csv_filenames = ['column_widths_enron', 'cell_annotations_enron', 'row_heights_enron', 'annotated_area_per_sheet',
                         'table_annotations_enron']
        print(os.listdir('.'))
        for filename in csv_filenames:
            csv_data[filename] = pd.read_csv(os.path.join(DIRECTORY_PATH , filename + '.csv'), header = 0, keep_default_na=False)
        print('Reading files successful.')

        translatorManager.generateInsertSQL(csv_data)
        dbconnector.commit()
        print("Translation finished.")


