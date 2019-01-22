import plotly.tools as tls
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

class Sheets_With_Label_Graph:
    count_tables = []

    def __init__(self, dbconnector):
        self.dbconnector = dbconnector
        self.labelCount = self._getLabelCount()

    def draw(self):
        plt.clf()
        plt.cla()
        plt.figure(figsize=[5.6, 3])

        height =  [x[0] for x in self.labelCount]

        # Choose the names of the bars
        bars = [x[1] for x in self.labelCount]
        y_pos = np.arange(len(bars))


        plt.xlabel('labels')
        plt.ylabel('count of spreadsheets')
        plt.ylim([0,1000])
        plt.xticks(y_pos, bars, rotation=40, horizontalalignment='right')
        plt.yticks([])
        plt.grid(color='#cccccc', linestyle='--', linewidth=0.5, zorder=0)
        ax = plt.bar(y_pos, height, zorder=3)

        rects = ax.patches
        labels = [x[0] for x in self.labelCount]

        # numbers on bars
        for rect, label in zip(rects, labels):
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width() / 2, height + 5, label,
                    ha='center', va='bottom')


        plt.tight_layout()

        # Show graphic
        plt.savefig('images/spreadsheets_with_label.png')


    def _getLabelCount(self):
        sql = 'select count(DISTINCT file_name), cell_label from cell_annotations group by cell_label'
        result = self.dbconnector.execute(sql)
        return result