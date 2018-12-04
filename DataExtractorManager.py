
class DataExtractorManager:

    def __init__(self, dbconnector):
        self.dbconnector = dbconnector
        self.AnnotationData = self._getRangesFromDB()

    def buildFormulaData(self):
        # for table in
        pass

    def _getRangesFromDB(self):
        sql = 'Select file_id, table_id, sheet_id, sheet_name, range_start, range_end from tables'
        annotationRanges = self.dbconnector.execute(sql)
        print (annotationRanges)
        return annotationRanges
