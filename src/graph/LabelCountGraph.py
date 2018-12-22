import plotly.tools as tls
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

class LabelCountGraph:
    count_tables = []

    def __init__(self, dbconnector):
        self.title = 'number of tables per sheet'
        self.xlabel = 'count of tables per sheet'
        self.ylabel = 'appearence in %'
        self.dbconnector = dbconnector
        self.labelCount = self._getLabelCount()

    def draw(self):
        plt.clf()
        height =  [x[0] for x in self.labelCount]

        # Choose the names of the bars
        bars = [x[1] for x in self.labelCount]
        y_pos = np.arange(len(bars))

        # Create bars
        plt.bar(y_pos, height)

        # Create names on the x-axis
        plt.xticks(y_pos, bars, color='orange', rotation=90)
        plt.yticks(color='orange')
        plt.subplots_adjust(bottom=0.2, top=0.99)

        # Show graphic
        plt.savefig('images/total_label_count.png')


    def _getLabelCount(self):
        sql = 'select count(DISTINCT sheet_name), cell_label from cell_annotations group by cell_label'
        result = self.dbconnector.execute(sql)
        return result