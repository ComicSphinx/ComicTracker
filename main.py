import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer, QTime
import design

class ComicTracker(QtWidgets.QMainWindow, design.Ui_MainWindow):

    timerIsEnabled = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.startButton.clicked.connect(self.startBtnClicked)

        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)

    def startBtnClicked(self):
        if (self.timerIsEnabled == False):
            self.startButton.setText("Stop")
            self.timerIsEnabled = True
            self.startTimer()
        elif (self.timerIsEnabled == True):
            self.startButton.setText("Start")
            self.timerIsEnabled = False
            self.stopTimer()

    def showTime(self):
        time = QTime(0, 0, 0)
        timeDisplay = time.toString('hh:mm:ss')
        self.label.setText(timeDisplay)

    def startTimer(self):
        self.timer.start(1000)
        self.startButton.setText("Stop")

    def stopTimer(self):
        self.startButton.setText("Start")
        self.timer.stop()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ComicTracker()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()