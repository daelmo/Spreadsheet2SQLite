import plotly.tools as tls
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.pyplot import gca

class VerticalGapGraph:
    count_tables = []

    def __init__(self, dbconnector):
        self.dbconnector = dbconnector
        self.tables_per_sheet = self._getTablesPerSheet()

    def draw(self):
        plt.clf()
        plt.cla()
        plt.figure(figsize=[5.6, 3])
        plt.xlim([-1, 15])
        plt.ylim([0, 150])
        plt.xticks(np.arange(0, 14, 1.0))
        plt.yticks([])
        plt.xlabel('gap size in row count')
        plt.ylabel('count of distances')
        #plt.grid(color='#cccccc', linestyle='--', linewidth=0.5, zorder=0)
        ax = sns.distplot(self.tables_per_sheet, bins=49, hist=True, kde=False,
                     hist_kws={ 'zorder': 3,  'alpha':1.0, 'align': 'left' })


        rects = ax.patches[:]
        labels = [int(h.get_height()) for h in ax.patches][:15]

        # numbers on bars
        for rect, label in zip(rects, labels):
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width() / 2, height + 2, label,
                    ha='center', va='bottom')

        plt.tight_layout()


        #plt.show()
        plt.savefig('images/vertical_gaps_between_tables.png')


    def _getTablesPerSheet(self):
        sql = 'select distance from vertical_table_distances'
        result = self.dbconnector.execute(sql)
        print(pd.DataFrame(result))
        return pd.DataFrame(result)
