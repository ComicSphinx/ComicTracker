from database.DatabaseUtilities import DatabaseUtilities as dbu
import matplotlib as mpl
import matplotlib.pyplot as plt

class PiePlot():

    def showPiePlot(self, records, minutes):
        self.configurePiePlot(self)
        plt.pie(minutes, labels=records, autopct='%1.0f%%')
        plt.show()

    def configurePiePlot(self):
        mpl.rcParams['toolbar'] = 'none'
        