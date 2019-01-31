import plotly.tools as tls
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.pyplot import gca


class HorizontalVerticalOrientationGraph:
    count_tables = []

    def __init__(self, dbconnector):
        self.dbconnector = dbconnector
        self.height = self._getOrientation()

    def draw(self):
        plt.clf()
        plt.cla()
        plt.figure(figsize=[5.6, 3])
        # plt.xlim([0, 10])
        plt.ylim([0, 370])
        plt.xticks([])
        plt.yticks([])

        plt.ylabel('count of tables')


        # Choose the names of the bars
        ax = plt.bar([1,2,3], self.height.values[0], zorder=3)


        rects = ax.patches[:3]
        labels = [int(h.get_height()) for h in ax.patches][:3]
        plt.xticks([1,2,3], ['horizontal', 'vertical', 'horizontal & vertical'])



        # numbers on bars
        for rect, label in zip(rects, labels):
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width() / 2, height + 5, label,
                     ha='center', va='bottom')

        plt.tight_layout()

        # plt.show()
        plt.savefig('images/orientation_of_tables_in_sheet.png')

    def _getOrientation(self):
        sql = '''with first_table as (
            Select 
                min(first_row * first_column), first_row, last_row, first_column, 
                last_column, file_name, table_name, sheet_name
            from tables
            group by sheet_name, file_name
            order by file_name),
            
            table_join as(
            select 
                t.first_row as t1_first_row, 
                t.first_column as t1_first_column, 
                t.last_row as t1_last_row, 
                t.last_column as t1_last_column,
                ft.first_row as t2_first_row, 
                ft.first_column as t2_first_column, 
                ft.last_row as t2_last_row,
                ft.last_column as t2_last_column,
                ft.sheet_name, 
                ft.file_name
            from tables t
            inner join first_table ft
            on t.file_name=ft.file_name and t.sheet_name = ft.sheet_name
            where t.table_name != ft.table_name),
            
             temp as(
            select 
            case 
                WHEN 
                    t1_first_column >  t2_last_column
                then 1
                else 0
            end as horizontal,
            case 
                WHEN 
                    t1_first_row > t2_last_row
                then 1
                else 0
            end as vertical,
            case 
                when	
                    t1_first_row > t2_last_row and 
                    t1_first_column >  t2_last_column
                    then 1
                    else 0 
            end as horizontal_vertical,
            file_name,
            sheet_name
            from table_join)
            
            select sum(horizontal), sum(vertical), sum(horizontal_vertical)
            from temp
        '''
        result = self.dbconnector.execute(sql)
        print(pd.DataFrame(result))
        return pd.DataFrame(result)