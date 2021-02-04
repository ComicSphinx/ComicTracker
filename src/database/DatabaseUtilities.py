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
    
    def addDataToDB(self, whatWillYouDoString, minutes):
        if (minutes > 0):
            connection, cursor = self.connectDB(self)
            insert = self.buildInsert(self, whatWillYouDoString, minutes)
            cursor.execute(insert)
            self.saveAndCloseDB(self,connection)

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
        result = cursor.fetchall()
        connection.close()
        return result

    def verifyTableEmptyByDate(self, year, month, day):
        connection, cursor = self.connectDB(self)
        select = self.buildSelect(self, year, month, day)
        cursor.execute(select)
        result = cursor.fetchall()
        connection.close()
        
        if result == []:
            return True
        else:
            return False
    
    def buildSelect(self, year, month, day):
        select = "SELECT * FROM"+self.tableName+"WHERE year = "
        select += str(year)
        select += " AND month = "
        select += str(month)
        select += " AND day = "
        select += str(day)
        return select

    def getMinutesRecordsByData(self, data):
        minutes = []
        records = []
        for i in range(len(data)):
            minutes.append(data[i][3])
            records.append(data[i][4])
        return minutes, records