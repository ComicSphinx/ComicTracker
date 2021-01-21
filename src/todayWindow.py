# @Author: Daniil Maslov
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from datetime import datetime as dt
import matplotlib.pyplot as plt
import sys
import os

import design.todayWindowDesign
from database.DatabaseUtilities import DatabaseUtilities as dbu

class TodayWindow(QtWidgets.QMainWindow, design.todayWindowDesign.Ui_todayWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QIcon("design/icon/icon.png"))
        self.createPlot()

    def createPlot(self):
        """ Get data from database """
        data = dbu.getDataByYearMonthDay(dbu, dt.now().year, dt.now().month, dt.now().day)
        records,minutes = self.prepareVariablesToPlot(data)
        plt.bar(records,minutes)
        plt.show()

    def prepareVariablesToPlot(self, data):
        x = []
        y = []
        for i in range(len(data)):
            """ Append str(record) to X """
            x.append(data[i][4])
            """ Append minutes to Y """
            y.append(data[i][3])
        return x,y


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = TodayWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()