#!/usr/bin/python
import pandas as pd
from src.DBConnector import DBConnector
from src.translator.TranslatorManager import TranslatorManager
from src.translator.CellAnnotationsTableTranslator import CellAnnotationsTableTranslator
from src.DataExtractorManager import DataExtractorManager


DIRECTORY_PATH = './data/'

if __name__ == '__main__':

    with DBConnector('sqlite.db') as dbconnector:

        translatorManager = TranslatorManager(dbconnector)
        translatorManager.generateCleanupSQL()
        translatorManager.generateCreateTableSQL()

        print('Start reading files.')
        csv_data = {}
        csv_filenames = ['column_widths_enron', 'cell_annotations_enron', 'row_heights_enron', 'annotated_area_per_file', 'test']
        for filename in csv_filenames:
            csv_data[filename] = pd.read_csv(DIRECTORY_PATH + filename + '.csv', header = 0, keep_default_na=False)
        print('Reading files successful.')

        translatorManager.generateInsertSQL(csv_data)
        dbconnector.commit()
        print("Translation finished.")


