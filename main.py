import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer, QTime
import design

class ComicTracker(QtWidgets.QMainWindow, design.Ui_MainWindow):
    # сделать time global и плюсовать секунды в startTimer
    timerIsEnabled = False
    time = QTime(0,0,0)
    timer = QTimer()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.startButton.clicked.connect(self.startBtnClicked)
        self.timer.timeout.connect(self.showTime)


    def startBtnClicked(self):
        if (self.timerIsEnabled == False):
            self.timerIsEnabled = True
            self.startTimer()
        elif (self.timerIsEnabled == True):
            self.timerIsEnabled = False
            self.stopTimer()

    def showTime(self): # обрабатывается дохрена раз в секунду
        self.label.setText(self.time.toString("hh:mm:ss"))
        self.time = self.time.addSecs(1)

    def startTimer(self):
        self.time = QTime(0,0,0)
        self.startButton.setText("Stop")
        self.timer.start(1000)

    def stopTimer(self):
        self.timer.stop()
        self.startButton.setText("Start")
        self.label.setText("00:00:00")


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ComicTracker()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()