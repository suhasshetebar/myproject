import sqlite3

from FindCard import ScanContent


class ScanDb:

    def __init__(self,DbPath):
        self.dbCon = sqlite3.connect(DbPath)
        self.ScanRes = {}

    def CollectTables(self):
        tables = []
        try:
            query = "SELECT name FROM sqlite_master WHERE type='table';"
            self.dbCon.cursor()
            tables = self.dbCon.execute(query).fetchall()
        finally:
            return tables

    def ScanTables(self):
        try:
            Tables = self.CollectTables()
            for table in Tables:
                self.ScanTable(table[0])
        finally:
            return self.ScanRes

    def ScanTable(self,table):
        try:
            query = "SELECT * FROM "+table
            self.dbCon.cursor()
            DbData = self.dbCon.execute(query).fetchall()
            if DbData[0]:
                Res = ScanContent(DbData.__str__())
                self.ScanRes.update(Res)
        except:
            pass
