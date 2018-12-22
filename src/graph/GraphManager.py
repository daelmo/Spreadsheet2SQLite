from src.graph.TableCountGraph import TableCountGraph
from src.graph.TableStats import TableStats
from src.graph.LabelCountGraph import LabelCountGraph

class GraphManager:
    graphsForDrawing = []
    dbconnector = None

    def __init__(self, dbconnector):
        self.dbconnector = dbconnector

        #tableCountGraph = TableCountGraph(dbconnector)
        tableStats = TableStats(dbconnector)
        #labelCountGraph = LabelCountGraph(dbconnector)

        self.graphsForDrawing = [ tableStats, ]

    def draw(self):
        for graph in self.graphsForDrawing:
            graph.draw()