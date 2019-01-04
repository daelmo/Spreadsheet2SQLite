#!/usr/bin/python
from src.DBConnector import DBConnector
from src.db_refining.RelationBuilder import RelationBuilder
from src.db_refining.ViewBuilder import ViewBuilder

if __name__ == '__main__':

    with DBConnector('sqlite.db') as dbconnector:

        relationBuilder = RelationBuilder(dbconnector)
        relationBuilder.buildRelations()

        viewBuilder = ViewBuilder(dbconnector)
        viewBuilder.buildViews()

        dbconnector.commit()

