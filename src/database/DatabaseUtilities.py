# @Author: Daniil Maslov
import sqlite3
import os
from datetime import datetime as dt

class DatabaseUtilities():

    databaseFilePath = "database/database.db"
    
    def verifyDatabaseExist(self):
        if (os.path.exists(self.databaseFilePath)):
            return 1
        else:
            return 0
    
    def createDB(self):
        """ Create database and connect to it """
        connection, cursor = self.connectDB(self)
        """ Create table in database (year, month | day | minutes | record)"""
        cursor.execute("CREATE TABLE records (year int, month int, day int, minutes int, record VARCHAR(60));")
        """ Save changes and close connection """
        self.saveAndCloseDB(self, connection)

    def connectDB(self):
        """ Connect to database """
        connection = sqlite3.connect(self.databaseFilePath)
        cursor = connection.cursor()
        return connection, cursor
    
    def saveAndCloseDB(self, connection):
        """ Save changes """
        connection.commit()
        """ Close connection """
        connection.close()
    
    def addDataToDB(self, whatWillYouDoString, minutes):
        if (minutes > 0):
            """ Connect to database """
            connection, cursor = self.connectDB(self)
            """ Build a request to the database"""
            request = self.buildInsertString(self, whatWillYouDoString, minutes)
            """ Add data to db """
            cursor.execute(request)
            """ Save changes and close connection """
            self.saveAndCloseDB(self,connection)

    def buildInsertString(self, string, minutes):
        tmpString = "INSERT INTO records VALUES("
        tmpString += str(dt.now().year)
        tmpString += "," + str(dt.now().month)
        tmpString += "," + str(dt.now().day)
        tmpString += "," + str(minutes)
        tmpString += ", '" + string + "');"
        return tmpString

    def getDataByYearMonthDay(self, year, month, day):
        connection, cursor = self.connectDB(self)
        request = "SELECT * FROM records WHERE year = "+str(year)+" AND month = "+str(month)+" AND day = "+str(day)+";"
        cursor.execute(request)
        result = cursor.fetchall()
        connection.close()
        return result

    def verifyTableEmpty(self, year, month, day):
        connection, cursor = self.connectDB(self)
        selectString = self.buildSelectString(self, year, month, day)
        cursor.execute(selectString)
        result = cursor.fetchall()
        connection.close()
        
        if result == []:
            return True
        else:
            return False
    
    def buildSelectString(self, year, month, day):
        selectString = "SELECT * FROM records WHERE year = "
        selectString += str(year)
        selectString += " AND month = "
        selectString += str(month)
        selectString += " AND day = "
        selectString += str(day)
        return selectString