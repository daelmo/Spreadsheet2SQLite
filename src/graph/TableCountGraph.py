import plotly.plotly as py
import plotly.tools as tls

import matplotlib.pyplot as plt
import numpy as np

class TableCountGraph:
    count_tables = []

    def __init__(self, dbconnector):
        self.title = 'number of tables per sheet'
        self.xlabel = 'count of tables per sheet'
        self.ylabel = 'appearence in %'
        self.dbconnector = dbconnector
        self._getGraphData()

    def draw(self):
        num_bins = len(self.tables_per_sheet)
        n, bins, patches = plt.hist( self.tables_per_sheet, num_bins, range=(1,10), facecolor='blue', normed= True, linewidth=1, edgecolor='green')
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.xticks(np.arange(min(self.tables_per_sheet), 10, 1.0))
        plt.savefig('images/table_count_per_file.png')

    def _getGraphData(self):
        self.tables_per_sheet = self._getTablesPerSheet()
        print(self.tables_per_sheet)

    def _getTablesPerSheet(self):
        sql = 'select count(c) from(Select count(distinct table_name) as c, file_name from cell_annotations where table_name is not NULL group by file_name)where c ==1'
        result = self.dbconnector.execute(sql)
        result = [nr for (nr,) in result]
        print('count of exact 1 table:' + str(result))

        sql = 'select count(c) from(Select count(distinct table_name) as c, file_name from cell_annotations where table_name is not NULL group by file_name)where c !=1'
        result = self.dbconnector.execute(sql)
        result = [nr for (nr,) in result]
        print('count of more than 1 table:' + str(result))

        sql = 'Select count(distinct table_name) from cell_annotations where table_name is not NULL group by file_name'
        result = self.dbconnector.execute(sql)
        result = [nr for (nr,) in result]
        return result