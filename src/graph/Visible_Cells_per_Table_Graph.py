import plotly.tools as tls
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

class Visible_Cells_per_Table_Graph:
    count_tables = []

    def __init__(self, dbconnector):
        self.dbconnector = dbconnector
        self.ratio_filled_cells_per_table = self._getVisibleCellsRatio()

    def draw(self):
        plt.clf()
        plt.cla()
        plt.figure(figsize= [5.6, 3])
        plt.xlabel('')
        plt.ylabel('')

        #plt.xlim([0,1])
        plt.ylim([0,680])
        plt.xticks([0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1])
        plt.yticks([])

        plt.grid(color='#cccccc', linestyle='--', linewidth=0.5, zorder=0)
        ax = sns.distplot(self.ratio_filled_cells_per_table, bins=10, hist=True, kde=False,
                     hist_kws={'zorder': 3, 'alpha':1.0, 'align': 'right'})
        plt.tight_layout()

        rects = ax.patches
        labels = [int(h.get_height()) for h in ax.patches]

        # numbers on bars
        for rect, label in zip(rects, labels):
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width() / 2, height + 5, label,
                    ha='center', va='bottom')

        #plt.show()
        plt.savefig('images/ratio_visible_cells_per_table.png')


    def _getVisibleCellsRatio(self):
        sql = '''		select 
            ROUND(
				CAST (coalesce(count_filled_visible_cells, 0) AS float) 
				/ 
				CAST (total_count_cells as float)
			, 1) as ratio_filled_cells
        from tables_visible_hidden_info'''
        result = self.dbconnector.execute(sql)
        print(pd.DataFrame(result))
        return pd.DataFrame(result)