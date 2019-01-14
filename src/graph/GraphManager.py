from src.graph.Table_per_Sheet_Graph import Table_per_Sheet_Graph
from src.graph.TableStats import TableStats
from src.graph.Sheets_With_Label_Graph import Sheets_With_Label_Graph
from src.graph.Visible_Cells_per_Table_Graph import Visible_Cells_per_Table_Graph
from src.graph.Density_Graph import Density_Graph
from src.graph.Coverage_Graph import Coverage_Graph

class GraphManager:
    graphsForDrawing = []
    dbconnector = None

    def __init__(self, dbconnector):
        self.dbconnector = dbconnector

        tableCountGraph = Table_per_Sheet_Graph(dbconnector)
        #tableStats = TableStats(dbconnector)
        labelCountGraph = Sheets_With_Label_Graph(dbconnector)
        hiddenCellsGraph = Visible_Cells_per_Table_Graph(dbconnector)
        densityGraph = Density_Graph(dbconnector)
        coverageGraph = Coverage_Graph(dbconnector)


        self.graphsForDrawing = [ tableCountGraph, labelCountGraph, hiddenCellsGraph, densityGraph, coverageGraph ]

    def draw(self):
        for graph in self.graphsForDrawing:
            graph.draw()