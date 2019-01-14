import plotly.tools as tls
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

class Density_Graph:
    count_tables = []

    def __init__(self, dbconnector):
        self.dbconnector = dbconnector
        self.density_per_table = self._getDensityValues()

    def draw(self):
        plt.clf()
        plt.cla()
        plt.figure(figsize= [5.6, 3])

        plt.xticks([max(self.density_per_table)-1])
        #plt.xlim(1000000000)

        plt.grid(color='#cccccc', linestyle='--', linewidth=0.5, zorder=0)
        sns.distplot(self.density_per_table, bins=1000, hist=True, kde=False, hist_kws={'zorder': 3, 'rwidth': 2, 'alpha':1.0})
        plt.tight_layout()

        #plt.show()
        plt.savefig('images/density_over_tables.png')


    def _getDensityValues(self):
        sql = '''select 
            ROUND(
				CAST (coalesce(count_filled_visible_cells, 0) AS float) 
				/			
				CAST ( coalesce(count_filled_hidden_cells,0) as float)
			, 0) as density
            from tables_visible_hidden_info'''
        result = self.dbconnector.execute(sql)
        print(pd.DataFrame(result))
        return pd.DataFrame(result)