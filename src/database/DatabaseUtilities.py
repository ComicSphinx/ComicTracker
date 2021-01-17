# @Author: Daniil Maslov
import sqlite3
import os
import datetime

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
        """ Create table in database (month | day | minutes | record)"""
        cursor.execute("CREATE TABLE records (month int, day int, minutes int, record VARCHAR(60))")
        """ Save changes and close connection """
        self.saveAndCloseDB(self, connection)

    def connectDB(self):
        """ Connect to database """
        connection = sqlite3.connect(self.databaseFilePath)
        cursor = connection.cursor()
        return connection, cursor
    
    def addDataToDB(self, whatWillYouDoString, minutes):
        if (minutes > 0):
            """ Connect to database """
            connection, cursor = self.connectDB(self)
            """ Build a request to the database"""
            request = self.buildRequestString(self, whatWillYouDoString, minutes)
            """ Add data to db """
            cursor.execute(request)
            """ Save changes and close connection """
            self.saveAndCloseDB(self,connection)

    def buildRequestString(self, string, minutes):
        tmpString = "INSERT INTO records VALUES("
        tmpString += str(datetime.datetime.now().month)
        tmpString += "," + str(datetime.datetime.now().day)
        tmpString += "," + str(minutes)
        tmpString += ", '" + string + "');"
        return tmpString
    
    def saveAndCloseDB(self, connection):
        """ Save changes """
        connection.commit()
        """ Close connection """
        connection.close()

    def getDataByDay(self, day):
        connection, cursor = self.connectDB(self)
        cursor.execute("SELECT * FROM records WHERE day == ", day)
        result = cursor.fetchall()
        return result