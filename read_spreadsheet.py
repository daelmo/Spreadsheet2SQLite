#!/usr/bin/python
import pandas as pd
from DBConnector import DBConnector
from Workbook2SQLTranslator import Workbook2SQLTranslator
from Sheet2TableTranslator import Sheet2TableTranslator
import glob



#DIRECTORY_PATH = 'ecir_annotated_files'
DIRECTORY_PATH = '.'

if __name__ == '__main__':

    with DBConnector('sqlite.db') as dbconnector:

        workbook2SQLTranslator = Workbook2SQLTranslator()
        sql = workbook2SQLTranslator.cleanup()
        dbconnector.execute(sql)

        sql = workbook2SQLTranslator.createTables()
        dbconnector.execute(sql)

        workbookPathsInDirectory = glob.glob(DIRECTORY_PATH + '/*.xlsx')
        for workbookPath in workbookPathsInDirectory:
            workbook = pd.ExcelFile(workbookPath)
            sheetdfs = {sheet: workbook.parse(sheet) for sheet in workbook.sheet_names}

            sql = workbook2SQLTranslator.translate(sheetdfs)
            dbconnector.execute(sql)



