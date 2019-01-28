
class ViewBuilder:

    def __init__(self, dbconnector):
        self.dbconnector = dbconnector

    def buildViews(self):
        self._buildTablesVisibleHiddenInfo()
        self._buildTablesOrientationInfo()


    def _buildTablesVisibleHiddenInfo(self):
        sql = '''create view tables_visible_hidden_info as
                with filled_visible_cells as (
                select count(*) as count_filled_visible_cells, table_name, file_name, sheet_name
                from cell_annotations 
                where table_name is not null and is_hidden = 0
                group by table_name, file_name, sheet_name
            ),
			filled_hidden_cells as(
				select count(*) as count_filled_hidden_cells, table_name, file_name, sheet_name
					from cell_annotations 
					where table_name is not null and is_hidden = 1
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
            ),
			joined_table as (
        
            select total_count_cells, count_filled_visible_cells, count_filled_hidden_cells, hidden_row_count, hidden_row_cells, hidden_column_count, hidden_column_cells, total.table_name, total.file_name, total.sheet_name
            from count_total_table_cells as total
            left join filled_visible_cells as filled_visible
            on total.table_name = filled_visible.table_name
            and total.file_name = filled_visible.file_name
            and total.sheet_name = filled_visible.sheet_name
			left join filled_hidden_cells as filled_hidden
            on total.table_name = filled_hidden.table_name
            and total.file_name = filled_hidden.file_name
            and total.sheet_name = filled_hidden.sheet_name
            left join count_hidden_rows as hidden_rows 
            on total.table_name = hidden_rows.table_name
            and total.file_name = hidden_rows.file_name
            and total.sheet_name = hidden_rows.sheet_name
            left join count_hidden_columns as hidden_columns 
            on total.table_name = hidden_columns.table_name
            and total.file_name = hidden_columns.file_name
            and total.sheet_name = hidden_columns.sheet_name)
			
			select 
                count_filled_visible_cells,
                count_filled_hidden_cells,
                total_count_cells,
                coalesce(hidden_row_cells,0) 
                + coalesce(hidden_column_cells,0) 
                - (coalesce(hidden_row_count,0) 
                * coalesce(hidden_column_count,0))
                as count_hidden_cells,
                coalesce(count_filled_visible_cells,0) 
                + coalesce(count_filled_hidden_cells,0) 
                as count_filled_cells,
                sheet_name,
                file_name,
                table_name
            from joined_table
        '''
        self.dbconnector.execute(sql)

    def _buildTablesOrientationInfo(self):
        sql= '''create view tables_orientation_info as 
with first_table as (
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
                ft.file_name,
				ft.table_name
            from tables t
            inner join first_table ft
            on t.file_name=ft.file_name and t.sheet_name = ft.sheet_name
            where t.table_name != ft.table_name)
            
             
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
			table_name,
            file_name,
            sheet_name
            from table_join'''
        self.dbconnector.execute(sql)

    def _buildTopLeftTables(self):
        sql = '''create view top_left_tables as 
            Select 
                min(first_row * first_column), first_row, last_row, first_column, 
                last_column, file_name, table_name, sheet_name
            from tables
            group by sheet_name, file_name
            order by file_name'''
        self.dbconnector.execute(sql)