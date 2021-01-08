""" @Author: Daniil Maslov """

import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer, QTime, QDate, QCalendar
import datetime
import sqlite3

import design

class MainWindow(QtWidgets.QMainWindow, design.Ui_MainWindow):

    timerIsEnabled = False
    time = QTime(0,0,0)
    timer = QTimer()
    databaseFilePath = "database/database.db"

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        
        """ Create database if it does not exist """
        if (self.verifyDatabaseExist() == False):
            self.createDB()

    def initUI(self):
        self.startButton.clicked.connect(self.startBtnClicked)
        self.timer.timeout.connect(self.showTime)

    def verifyDatabaseExist(self):
        if (os.path.exists(self.databaseFilePath)):
            return 1
        else:
            return 0

    def createDB(self):
        """ Create database and connect to it """
        connection, cursor = self.connectDB()
        """ Create table in database """
        cursor.execute("CREATE TABLE records (month int, day int, minutes int, record VARCHAR(60))")
        """ Save changes and close connection """
        self.closeDB(connection)

    def connectDB(self):
        """ Connect to database """
        connection = sqlite3.connect(self.databaseFilePath)
        cursor = connection.cursor()
        return connection, cursor

    def closeDB(self, connection):
        """ Save changes """
        connection.commit()
        """ Close connection """
        connection.close()

    def startBtnClicked(self):
        if (self.timerIsEnabled == False):
            self.timerIsEnabled = True
            self.startTimer()
        elif (self.timerIsEnabled == True):
            self.timerIsEnabled = False
            self.stopTimer()

    def showTime(self):
        self.clock.setText(self.time.toString("hh:mm:ss"))
        self.time = self.time.addSecs(1)

    def startTimer(self):
        self.time = QTime(0,0,0)
        self.startButton.setText("Stop")
        self.whatWillYouDo.setEnabled(False)
        self.timer.start(1000)

    def stopTimer(self):
        self.handleData(self.time.hour(), self.time.minute())
        self.timer.stop()
        self.startButton.setText("Start")
        self.clock.setText("00:00:00")
        self.whatWillYouDo.setEnabled(True)
        self.whatWillYouDo.setText("")

    def handleData(self, hours, minutes):
        self.addDataToDB(self.getDataFromLabel(), self.computeMinutes(hours, minutes))

    def getDataFromLabel(self):
        """ Return text from whatWillYouDo (label) """
        return self.whatWillYouDo.toPlainText()

    def computeMinutes(self, hours, minutes):
        if (hours == 0):
            return minutes
        elif (hours > 0):
            tmp = hours * 60
            minutes = minutes + tmp
            return minutes

    def addDataToDB(self, whatWillYouDoString, minutes):
        if (minutes > 0):
            """ Connect to database """
            connection, cursor = self.connectDB()
            """ Build a request to the database"""
            request = self.buildRequestString(whatWillYouDoString, minutes)
            """ Add data to db """
            cursor.execute(request)
            """ Save changes and close connection """
            self.closeDB(connection)

    def buildRequestString(self, string, minutes):
        tmpString = "INSERT INTO records VALUES("
        tmpString += str(datetime.datetime.now().month)
        tmpString += "," + str(datetime.datetime.now().day)
        tmpString += "," + str(minutes)
        tmpString += ", '" + string + "');"
        return tmpString

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()