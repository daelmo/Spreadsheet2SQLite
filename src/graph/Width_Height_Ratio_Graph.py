import plotly.tools as tls
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


class Width_Height_Ratio_Graph:
    count_tables = []

    def __init__(self, dbconnector):
        self.dbconnector = dbconnector
        self.width_height_ratio_per_table = self._getWidthHeightRatios()

    def draw(self):
        plt.clf()
        plt.cla()
        plt.figure(figsize=[5.6, 3])
        plt.xlim([0, 5.05])
        plt.ylim([0,770])
        plt.xlabel('ratio value')
        plt.ylabel('count of tables')

       # plt.xticks(np.arange(0, 2, step=0.2))
        plt.yticks([])
        plt.grid(color='#cccccc', linestyle='--', linewidth=0.5, zorder=0)
        ax = sns.distplot(self.width_height_ratio_per_table, bins=31, hist=True, kde=False,
                     hist_kws={'zorder': 3, 'alpha': 1.0})


        rects = ax.patches[:15]
        labels = [int(h.get_height()) for h in ax.patches][:15]

        # numbers on bars
        for rect, label in zip(rects, labels):
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width() / 2, height + 5, label,
                    ha='center', va='bottom')

        plt.tight_layout()

        # plt.show()
        plt.savefig('images/width_height_ratio_over_tables.png')

    def _getWidthHeightRatios(self):
        sql = '''select 
            ROUND(
            CAST(last_column - first_column +1 as float)
            /
            CAST (last_row-first_row +1 as float) 
            , 1)
            from tables
            '''
        result = self.dbconnector.execute(sql)
        print(pd.DataFrame(result))
        return pd.DataFrame(result)