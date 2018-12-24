import plotly.tools as tls
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

class LabelCountGraph:
    count_tables = []

    def __init__(self, dbconnector):
        self.title = 'number of tables per sheet'
        self.xlabel = 'annotated cell labels'
        self.ylabel = 'count of cells'
        self.dbconnector = dbconnector
        self.labelCount = self._getLabelCount()

    def draw(self):
        plt.clf()
        plt.cla()
        plt.close()
        height =  [x[0] for x in self.labelCount]

        # Choose the names of the bars
        bars = [x[1] for x in self.labelCount]
        y_pos = np.arange(len(bars))

        # Create bars

        # Create names on the x-axis
        plt.xticks(y_pos, bars, color='orange', rotation=40, horizontalalignment='right')
        plt.yticks(color='orange')
        plt.grid(color='#cccccc', linestyle='--', linewidth=0.5, zorder=0)
        plt.bar(y_pos, height, zorder=3)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)

        plt.tight_layout()

        # Show graphic
        plt.savefig('images/total_label_count.png')


    def _getLabelCount(self):
        sql = 'select count(DISTINCT sheet_name), cell_label from cell_annotations group by cell_label'
        result = self.dbconnector.execute(sql)
        return result