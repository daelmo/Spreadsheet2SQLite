import pandas as pd
class TableStats:

    def __init__(self, dbconnector):
        self.dbconnector = dbconnector

    def draw(self):
        #self._printTableCOuntPerSheet()
        #self._printCountInnerOuterCells()
        #self._printLabelDistribution()
        self._CountSpreadsheetPerLabel()

    def _printCountInnerOuterCells(self):
        sql='select count(*) from cell_annotations WHERE (table_name is null or table_name = "");'
        result_outer = self.dbconnector.execute(sql)

        sql = 'select count(*) from cell_annotations WHERE (table_name is not null and table_name != "");'
        result_inner = self.dbconnector.execute(sql)

        [(result_inner,)] = result_inner
        [(result_outer,)] = result_outer

        print('count of out of table cells:' + str(result_outer) + ' in percent:' + str(
            result_outer / (result_inner + result_outer)))
        print('count of in table cells:' + str(result_inner) + ' in percent ' + str(
            result_inner / (result_outer + result_inner)))



    def _printTableCOuntPerSheet(self):
        sql = 'select count(c) from(Select count(distinct table_name) as c, file_name from cell_annotations where table_name is not NULL group by file_name)where c ==1'
        result_one = self.dbconnector.execute(sql)

        sql = 'select count(c) from(Select count(distinct table_name) as c, file_name from cell_annotations where table_name is not NULL group by file_name)where c !=1'
        result_many = self.dbconnector.execute(sql)

        print (result_many)
        [(result_one,)] = result_one
        [(result_many,)] = result_many
        print(result_many)
        print('count of exact 1 table:' + str(result_one) + ' in percent:' + str(
            result_one / (result_one + result_many)))
        print('count of more than 1 table:' + str(result_many) + ' in percent ' + str(
            result_many / (result_many + result_one)))

    def _printLabelDistribution(self):
        sql = 'select count(*), cell_label from cell_annotations group by cell_label'
        result = self.dbconnector.execute(sql)
        print(pd.DataFrame(result))

    def _CountSpreadsheetPerLabel(self):
        sql = 'select count(DISTINCT sheet_name), cell_label from cell_annotations group by cell_label'
        result = self.dbconnector.execute(sql)
        print(pd.DataFrame(result))


