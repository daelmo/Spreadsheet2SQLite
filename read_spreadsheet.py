#!/usr/bin/python
import xlrd
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
            workbook = xlrd.open_workbook(workbookPath)
            sql = workbook2SQLTranslator.translate(workbook.sheet_by_name('Range_Annotations_Data'))
            dbconnector.execute(sql)



