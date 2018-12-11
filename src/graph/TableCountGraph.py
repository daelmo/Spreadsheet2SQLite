import plotly.plotly as py
import plotly.tools as tls

import matplotlib.pyplot as plt
import numpy as np

class TableCountGraph:
    count_tables = []

    def __init__(self):
        self.title = 'number of tables per sheet'
        self.xlabel = 'count of tables per sheet'
        self.ylabel = 'appearence in %'
        self._getGraphData()



    def draw(self):
        y = [12, 6, 4 , 3, 2, 1,1 ]
        num_bins = 7
        n, bins, patches = plt.hist( y, num_bins, facecolor='blue', alpha=0.5, normed=True, linewidth=1, edgecolor='green')
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.show()

    def _getGraphData(self):
        self.tables_per_sheet = self._getTablesPerSheet()
        self.totalCountOfTables = self._getTotalCountOfTables()


    def _getTablesPerSheet(self):
        return (1,2,2)

    def _getTotalCountOfTables(self):
        return 5