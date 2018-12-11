#!/usr/bin/python
import pandas as pd
from DBConnector import DBConnector
from TranslatorManager import TranslatorManager
from CellAnnotationsTableTranslator import CellAnnotationsTableTranslator
from DataExtractorManager import DataExtractorManager
import glob



#DIRECTORY_PATH = 'ecir_annotated_files'
DIRECTORY_PATH = 'data/'

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

        # use data from database for info extraction

        dataExtractorManager = DataExtractorManager(dbconnector)
        dataExtractorManager.buildFormulaData()


        dbconnector.commit()




