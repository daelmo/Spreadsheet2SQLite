#!/usr/bin/python
import pandas as pd
from DBConnector import DBConnector
from SQLTranslatorManager import SQLTranslatorManager
from ToTableTableTranslator import ToTableTableTranslator
import glob



#DIRECTORY_PATH = 'ecir_annotated_files'
DIRECTORY_PATH = '.'

if __name__ == '__main__':

    with DBConnector('sqlite.db') as dbconnector:

        translatorManager = SQLTranslatorManager(dbconnector)
        translatorManager.generateCleanupSQL()
        translatorManager.generateCreateTableSQL()

        workbookPathsInDirectory = glob.glob(DIRECTORY_PATH + '/*.xlsx')
        for workbookPath in workbookPathsInDirectory:
            print("Start translating " + workbookPath + " in SQL:")
            workbook = pd.ExcelFile(workbookPath)
            sheetdfs = {sheet: workbook.parse(sheet) for sheet in workbook.sheet_names}
            translatorManager.generateInsertSQL(sheetdfs)
            print("Translation successful.")




