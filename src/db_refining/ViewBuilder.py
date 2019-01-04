
class ViewBuilder:

    def __init__(self, dbconnector):
        self.dbconnector = dbconnector

    def buildViews(self):
        self._buildTablesVisibleHiddenInfo()


    def _buildTablesVisibleHiddenInfo(self):
        sql = '''create view tables_visible_hidden_info as
                with filled_in_cells as (
                select count(*) as filled_cell_count, table_name, file_name, sheet_name
                from cell_annotations 
                where table_name is not null and is_hidden = 0
                group by table_name, file_name, sheet_name
            ),
            count_total_table_cells as (
                select (last_row-first_row+1) * (last_column-first_column +1) as total_count_cells , 
                    table_name,
                    sheet_name,
                    file_name 
                from tables
            ),
            count_hidden_rows as(
                select 
                count(*) as hidden_row_count,  
                count(*) * (t.last_column - t.first_column +1) as hidden_row_cells , 
                table_name, 
                rh.sheet_name, 
                rh.file_name 
                from row_heights rh
                inner join tables t
                on rh.file_name = t.file_name and rh.sheet_name = t.sheet_name
                where rh.is_hidden = 1 and rh.row_index >= t.first_row and rh.row_index <= t.last_row
                group by rh.sheet_name, rh.file_name, t.sheet_name, t.table_name, t.file_name
            ),
            count_hidden_columns as(
                select 
                    count(*) as hidden_column_count, 
                    count(*) * (t.last_row - t.first_row +1) as hidden_column_cells, 
                    table_name, cw.sheet_name, cw.file_name
                from column_widths cw
                inner join tables t
                on cw.file_name = t.file_name and cw.sheet_name = t.sheet_name
                where cw.is_hidden = 1 and cw.column_index >= t.first_column and cw.column_index <= t.last_column
                group by t.table_name, t.sheet_name, t.file_name, cw.sheet_name, cw.file_name
            )
        
            select total_count_cells, filled_cell_count, hidden_row_count, hidden_row_cells, hidden_column_count, hidden_column_cells, total.table_name, total.file_name, total.sheet_name
            from count_total_table_cells as total
            left join filled_in_cells as filled 
            on total.table_name = filled.table_name
            and total.file_name = filled.file_name
            and total.sheet_name = filled.sheet_name
            left join count_hidden_rows as hidden_rows 
            on total.table_name = hidden_rows.table_name
            and total.file_name = hidden_rows.file_name
            and total.sheet_name = hidden_rows.sheet_name
            left join count_hidden_columns as hidden_columns 
            on total.table_name = hidden_columns.table_name
            and total.file_name = hidden_columns.file_name
            and total.sheet_name = hidden_columns.sheet_name
        '''
        self.dbconnector.execute(sql)