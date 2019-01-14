import plotly.tools as tls
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

class Coverage_Graph:
    count_tables = []

    def __init__(self, dbconnector):
        self.dbconnector = dbconnector
        self.coverage_per_table = self._getCoverageValues()

    def draw(self):
        plt.clf()
        plt.cla()
        plt.figure(figsize= [5.6, 3])
        #plt.xlim([0,1.1])

        plt.xticks([ 0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1])
        plt.grid(color='#cccccc', linestyle='--', linewidth=0.5, zorder=0)
        sns.distplot(self.coverage_per_table, bins=10, hist=True, kde=False,
                     hist_kws={'zorder': 3,  'alpha': 1.0, 'align': 'right'})
        plt.tight_layout()

        #plt.show()
        plt.savefig('images/coverage_over_tables.png')


    def _getCoverageValues(self):
        sql = '''with all_visible_filled_cells as (
            select count(*) as all_visible_filled, sheet_name, file_name
            from cell_annotations
            where is_hidden=0
            group by sheet_name, file_name),
            in_table_filled_cells as (
            select count(*) as in_table_filled , sheet_name, file_name
            from cell_annotations
            where is_hidden=0 and table_name is not null
            group by sheet_name, file_name)
            
            select 
                ROUND(
                CAST( in_table_filled as float) 
                / 
                CAST (all_visible_filled as float)
                , 1 )
            from in_table_filled_cells as in_table
            join all_visible_filled_cells as all_cells
            on all_cells.sheet_name = in_table.sheet_name and all_cells.file_name = in_table.file_name
            '''
        result = self.dbconnector.execute(sql)
        print(pd.DataFrame(result))
        return pd.DataFrame(result)