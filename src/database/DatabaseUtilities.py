# @Author: Daniil Maslov (ComicSphinx)
import sqlite3
import os
from datetime import datetime as dt

class DatabaseUtilities():

    databaseFilePath = "database/database.db"
    tableName = " records "
    
    def verifyDatabaseExist(self):
        if (os.path.exists(self.databaseFilePath)):
            return 1
        else:
            return 0
    
    def createDB(self):
        connection, cursor = self.connectDB(self)
        cursor.execute("CREATE TABLE"+self.tableName+"(year int, month int, day int, minutes int, record VARCHAR(60));")
        self.saveAndCloseDB(self, connection)

    def connectDB(self):
        connection = sqlite3.connect(self.databaseFilePath)
        cursor = connection.cursor()
        return connection, cursor
    
    def saveAndCloseDB(self, connection):
        connection.commit()
        connection.close()
    
    def executeCommand(self, insert):
        connection, cursor = self.connectDB(self)
        cursor.execute(insert)
        output = cursor.fetchall()
        self.saveAndCloseDB(self,connection)
        return output

    def buildInsert(self, string, minutes):
        insert = "INSERT INTO"+self.tableName+"VALUES("
        insert += str(dt.now().year)
        insert += "," + str(dt.now().month)
        insert += "," + str(dt.now().day)
        insert += "," + str(minutes)
        insert += ", '" + string + "');"
        return insert

    def getDataByYearMonthDay(self, year, month, day):
        connection, cursor = self.connectDB(self)
        select = "SELECT * FROM"+self.tableName+"WHERE year = "+str(year)+" AND month = "+str(month)+" AND day = "+str(day)+";"
        cursor.execute(select)        
        output = cursor.fetchall()
        connection.close()
        return output

    def dataIsNotExist(self, select):
        connection, cursor = self.connectDB(self)
        cursor.execute(select)
        output = cursor.fetchall()
        connection.close()
        
        if (output == []):
            return True
        else:
            return False
    
    def buildSelect(self, year = None, month = None, day = None, string = None):
        select = "SELECT * FROM"+self.tableName
        if year != None:
            select += "WHERE year = "
            select += str(year)
        if month != None:
            select += " AND month = "
            select += str(month)
        if day != None:
            select += " AND day = "
            select += str(day)
        if string != None:
            select += " AND record = '"
            select += string + "';"
        return select

    def getMinutesRecordsByData(self, data):
        minutes = []
        records = []
        for i in range(len(data)):
            minutes.append(data[i][3])
            records.append(data[i][4])
        return minutes, records