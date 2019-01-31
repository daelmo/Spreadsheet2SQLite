from src.graph.Table_per_Sheet_Graph import Table_per_Sheet_Graph
from src.graph.TableStats import TableStats
from src.graph.Sheets_With_Label_Graph import Sheets_With_Label_Graph
from src.graph.Visible_Cells_per_Table_Graph import Visible_Cells_per_Table_Graph
from src.graph.CoverageGraph import Coverage_Graph
from src.graph.Width_Height_Ratio_Graph import Width_Height_Ratio_Graph
from src.graph.HorizontalVerticalOrientationGraph import HorizontalVerticalOrientationGraph
from src.graph.VerticalGapGraph import VerticalGapGraph
from src.graph.HorizontalGapGraph import HorizontalGapGraph
import matplotlib.pyplot as plt

class GraphManager:
    graphsForDrawing = []
    dbconnector = None
    plt.rcParams.update({'font.size': 14})

    def __init__(self, dbconnector):
        self.dbconnector = dbconnector

        tableCountGraph = Table_per_Sheet_Graph(dbconnector)
        tableStats = TableStats(dbconnector)
        labelCountGraph = Sheets_With_Label_Graph(dbconnector)
        hiddenCellsGraph = Visible_Cells_per_Table_Graph(dbconnector)
        coverageGraph = Coverage_Graph(dbconnector)
        widthHeightGraph = Width_Height_Ratio_Graph(dbconnector)
        orientationGraph = HorizontalVerticalOrientationGraph(dbconnector)
        verticalGapsGraph = VerticalGapGraph(dbconnector)
        horizontalGapGraph = HorizontalGapGraph(dbconnector)


        self.graphsForDrawing = [ horizontalGapGraph, verticalGapsGraph , tableCountGraph, labelCountGraph, hiddenCellsGraph, coverageGraph, widthHeightGraph, orientationGraph,  tableStats ]

    def draw(self):
        for graph in self.graphsForDrawing:
            graph.draw()