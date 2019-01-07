import plotly.tools as tls
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

class HiddenCellsGraph:
    count_tables = []

    def __init__(self, dbconnector):
        self.xlabel = 'ration of filled in cells per table'
        self.ylabel = 'count of sheets'
        self.dbconnector = dbconnector
        self.ratio_filled_cells_per_table = self._getVisibleCellsRatio()

    def draw(self):
        plt.clf()
        plt.cla()
        plt.figure(figsize= [3, 3])

        num_bins = range(0,100)

        plt.grid(color='#cccccc', linestyle='--', linewidth=0.01, zorder=0)
        sns.distplot(self.ratio_filled_cells_per_table, bins=num_bins, hist=True, kde=False, hist_kws={'align': 'left', 'zorder': 3, 'rwidth': 0.01, 'alpha':1.0})
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.tight_layout()

        plt.xlim([0,1])
        plt.xticks([0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1])
        #plt.show()
        plt.savefig('images/ratio_hidden_cells_per_table.png')


    def _getVisibleCellsRatio(self):
        sql = '''select 
            ROUND(CAST (coalesce(filled_cell_count, 0) AS float) / CAST (
            total_count_cells
            - coalesce(hidden_row_cells,0) 
            - coalesce(hidden_column_cells,0) 
            + (coalesce(hidden_row_count,0) 
            * coalesce(hidden_column_count,0))
            as float), 1) as ratio_filled_cells
            from tables_visible_hidden_info'''
        result = self.dbconnector.execute(sql)
        print(pd.DataFrame(result))
        return pd.DataFrame(result)