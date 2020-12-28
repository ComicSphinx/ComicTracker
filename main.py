import sys
from PyQt5 import QtWidgets
import design

class ComicTracker(QtWidgets.QMainWindow, design.Ui_MainWindow): # to use design.py
    def __init__(self):
        super().__init__()
        self.setupUi(self) # initialize design.py

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ComicTracker()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()