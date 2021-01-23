# @Author: Daniil Maslov

import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer, QTime, QDate, QCalendar
from PyQt5.QtGui import QIcon
from datetime import datetime as dt

import design.mainWindowDesign
from database.DatabaseUtilities import DatabaseUtilities as dbu
from Plot import Plot as pt

class MainWindow(QtWidgets.QMainWindow, design.mainWindowDesign.Ui_MainWindow):

    timerIsEnabled = False
    time = QTime(0,0,0)
    timer = QTimer()


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        
        """ Create database if it does not exist """
        if (dbu.verifyDatabaseExist(dbu) == False):
            dbu.createDB(dbu)

    def initUI(self):
        self.setWindowIcon(QIcon("design/icon/icon.png"))
        self.startButton.clicked.connect(self.startBtnClicked)
        self.todayButton.clicked.connect(self.todayBtnClicked)
        self.timer.timeout.connect(self.showTime)

    def startBtnClicked(self):
        if (self.timerIsEnabled == False):
            self.timerIsEnabled = True
            self.startTimer()
        elif (self.timerIsEnabled == True):
            self.timerIsEnabled = False
            self.stopTimer()

    def todayBtnClicked(self):
        pt.showPlot(pt, dt.now().year, dt.now().month, dt.now().day)

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
        dbu.addDataToDB(dbu, self.getDataFromLabel(), self.computeMinutes(hours, minutes))

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

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()