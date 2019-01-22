import plotly.tools as tls
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.pyplot import gca

class Table_per_Sheet_Graph:
    count_tables = []

    def __init__(self, dbconnector):
        self.dbconnector = dbconnector
        self.tables_per_sheet = self._getTablesPerSheet()

    def draw(self):
        plt.clf()
        plt.cla()
        plt.figure(figsize=[5.6, 3])
        plt.xlim([0, 10])
        plt.ylim([0, 750])
        plt.xticks(np.arange(0, 10, 1.0))
        plt.yticks([])
        plt.xlabel('count of tables')
        plt.ylabel('count of spreadsheets')
        plt.grid(color='#cccccc', linestyle='--', linewidth=0.5, zorder=0)
        ax = sns.distplot(self.tables_per_sheet, bins=124, hist=True, kde=False,
                     hist_kws={ 'zorder': 3,  'alpha':1.0, 'align': 'left' })


        rects = ax.patches[:10]
        labels = [int(h.get_height()) for h in ax.patches][:10]

        # numbers on bars
        for rect, label in zip(rects, labels):
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width() / 2, height + 5, label,
                    ha='center', va='bottom')

        plt.tight_layout()


        #plt.show()
        plt.savefig('images/table_count_per_file.png')


    def _getTablesPerSheet(self):
        sql = 'Select count(distinct table_name) from cell_annotations where table_name is not NULL group by file_name'
        result = self.dbconnector.execute(sql)
        print(pd.DataFrame(result))
        return pd.DataFrame(result)