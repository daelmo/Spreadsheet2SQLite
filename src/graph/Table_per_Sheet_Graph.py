import plotly.tools as tls
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

class Table_per_Sheet_Graph:
    count_tables = []

    def __init__(self, dbconnector):
        self.dbconnector = dbconnector
        self.tables_per_sheet = self._getTablesPerSheet()

    def draw(self):
        plt.clf()
        plt.cla()
        plt.figure(figsize=[5.6, 3])

        num_bins = range(0,11)

        plt.grid(color='#cccccc', linestyle='--', linewidth=0.5, zorder=0)
        sns.distplot(self.tables_per_sheet, bins=num_bins, hist=True, kde=False, hist_kws={'align':'left', 'zorder': 3, 'rwidth': 0.8, 'alpha':1.0 })
        plt.tight_layout()

        plt.xlim([0,10])
        plt.xticks(np.arange(0, 10, 1.0))
        #plt.show()
        plt.savefig('images/table_count_per_file.png')


    def _getTablesPerSheet(self):
        sql = 'Select count(distinct table_name) from cell_annotations where table_name is not NULL group by file_name'
        result = self.dbconnector.execute(sql)
        print(pd.DataFrame(result))
        return pd.DataFrame(result)