from src.graph.TableCountGraph import TableCountGraph


class GraphManager:
    graphsForDrawing = []
    dbconnector = None

    def __init__(self, dbconnector):
        self.dbconnector = dbconnector

        tableCountGraph = TableCountGraph()
        self.graphsForDrawing = [tableCountGraph]

    def draw(self):
        for graph in self.graphsForDrawing:
            graph.draw()