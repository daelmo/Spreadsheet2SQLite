import plotly.tools as tls
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

class TableCountGraph:
    count_tables = []

    def __init__(self, dbconnector):
        self.title = 'number of tables per sheet'
        self.xlabel = 'count of tables per sheet'
        self.ylabel = 'appearence in %'
        self.dbconnector = dbconnector
        self.tables_per_sheet = self._getTablesPerSheet()

    def draw(self):
        plt.clf()
        num_bins = len(self.tables_per_sheet)
        # n, bins, patches = plt.hist( self.tables_per_sheet, num_bins, range=(1,10), facecolor='blue', normed= True, linewidth=1, edgecolor='green')
        sns.distplot(self.tables_per_sheet, bins=num_bins, hist=True, kde=False, axlabel=self.xlabel)
        plt.tight_layout()
        plt.xlim([0,10])
        plt.xticks(np.arange(min(self.tables_per_sheet), 11, 1.0))
        #plt.show()
        plt.savefig('images/table_count_per_file.png')


    def _getTablesPerSheet(self):
        sql = 'Select count(distinct table_name) from cell_annotations where table_name is not NULL group by file_name'
        result = self.dbconnector.execute(sql)
        print(pd.DataFrame(result))
        return pd.DataFrame(result)