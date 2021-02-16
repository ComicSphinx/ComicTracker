# @Author: Daniil Maslov

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtGui import QIcon
from datetime import datetime as dt

import design.mainWindowDesign
from database.DatabaseUtilities import DatabaseUtilities as dbu
from BarPlot import BarPlot as bpt
from PiePlot import PiePlot as ppt

class MainWindow(QtWidgets.QMainWindow, design.mainWindowDesign.Ui_MainWindow):

    timerIsEnabled = False
    time = QTime(0,0,0)
    timer = QTimer()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        
        # Create database if it does not exist
        if (dbu.verifyDatabaseExist(dbu) == False):
            dbu.createDB(dbu)

    def initUI(self):
        self.setWindowIcon(QIcon("images/icons/icon.png"))

        self.btn_start.clicked.connect(self.clicked_startBtn)
        self.btn_today.clicked.connect(self.clicked_todayBtn)
        self.timer.timeout.connect(self.countTime)

    def clicked_startBtn(self):
        if (self.timerIsEnabled == False):
            self.startTimer()
            self.btn_start.setText("Stop")
            self.textEdit_WhatWillYouDo.setEnabled(False)
        else:
            self.timer.stop()

            minutes = self.computeMinutes(self.time.hour(), self.time.minute())
            record = self.getDataFromTextEdit(self.textEdit_WhatWillYouDo)

            if (minutes > 0):
                insert = dbu.buildInsert(dbu, record, minutes)
                dbu.executeCommand(dbu, insert)
                
            self.refreshItems()
        # Reverse timerIsEnabled value
        self.timerIsEnabled = not self.timerIsEnabled

    def clicked_todayBtn(self):
        select = dbu.buildSelect(dbu, dt.now().year, dt.now().month, dt.now().day)
        if (dbu.dataIsNotExist(dbu, select)):
            self.showMessageTableEmpty()
        else:
            data = dbu.getDataByYearMonthDay(dbu, dt.now().year, dt.now().month, dt.now().day)
            minutes,records = dbu.getMinutesRecordsByData(bpt, data)
            #bpt.showBarPlot(bpt, records, minutes)
            ppt.showPiePlot(ppt, records, minutes)
    
    def countTime(self):
        self.clock.setText(self.time.toString("hh:mm:ss"))
        self.time = self.time.addSecs(1)

    def startTimer(self):
        self.time = QTime(0,0,0)
        self.timer.start(1000)

    def getDataFromTextEdit(self, textEdit):
        return textEdit.toPlainText()

    def computeMinutes(self, hours, minutes):
        if (hours == 0):
            return minutes
        else:
            hours = hours * 60
            minutes = minutes + hours
            return minutes

    def refreshItems(self):
        self.clock.setText("00:00:00")
        self.btn_start.setText("Start")
        self.textEdit_WhatWillYouDo.setText("")
        self.textEdit_WhatWillYouDo.setEnabled(True)

    def showMessageTableEmpty(self):
        message = QMessageBox()
        message.setText("Table is empty, start working right now!")
        message.setIcon(QMessageBox.Warning)
        message.exec()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()