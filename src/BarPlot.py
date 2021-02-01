# @Author: Daniil Maslov (ComicSphinx)

from database.DatabaseUtilities import DatabaseUtilities as dbu
import matplotlib as mpl
import matplotlib.pyplot as plt

class BarPlot():
    
    def showBarPlot(self, records, minutes):
        self.configureBarPlot(self, minutes)
        plt.bar(records, minutes, align='center', width=0.3)
        plt.show()

    def configureBarPlot(self, minutes):
        mpl.rcParams['toolbar'] = 'none'
        plt.yticks(minutes)
        plt.subplots_adjust(bottom = 0.1, top = 0.95)
        plt.ylabel("Minutes")