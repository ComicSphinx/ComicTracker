# @Author: Daniil Maslov
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
import sys
import os

import design.todayWindowDesign

class TodayWindow(QtWidgets.QMainWindow, design.todayWindowDesign.Ui_todayWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = TodayWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()