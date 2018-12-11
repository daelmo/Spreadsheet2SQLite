#!/usr/bin/python
from src.GraphManager import GraphManager
from src.DBConnector import DBConnector

if __name__ == '__main__':

    with DBConnector('sqlite.db') as dbconnector:
        graphManager = GraphManager(dbconnector)
        graphManager.draw()