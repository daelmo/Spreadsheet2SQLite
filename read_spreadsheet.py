#!/usr/bin/python
import pandas as pd
from DBConnector import DBConnector
from File2SQLManager import File2SQLManager
from Sheet2TableTranslator import Sheet2TableTranslator
import glob



#DIRECTORY_PATH = 'ecir_annotated_files'
DIRECTORY_PATH = '.'

if __name__ == '__main__':

    with DBConnector('sqlite.db') as dbconnector:

        file2SQLTranslator = File2SQLManager(dbconnector)
        file2SQLTranslator.generateCleanupSQL()
        file2SQLTranslator.generateCreateTableSQL()

        workbookPathsInDirectory = glob.glob(DIRECTORY_PATH + '/*.xlsx')
        for workbookPath in workbookPathsInDirectory:
            print("Start translating " + workbookPath + " in SQL:")
            workbook = pd.ExcelFile(workbookPath)
            sheetdfs = {sheet: workbook.parse(sheet) for sheet in workbook.sheet_names}
            file2SQLTranslator.generateInsertSQL(sheetdfs)
            print("Translation successful.")




