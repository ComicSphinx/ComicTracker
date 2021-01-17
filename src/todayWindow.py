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
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QIcon("design/icon/icon.png"))

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = TodayWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()