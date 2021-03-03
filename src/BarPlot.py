# @Author: Daniil Maslov (ComicSphinx)

import matplotlib as mpl
import matplotlib.pyplot as plt
from Plot import Plot

class BarPlot(Plot):
    
    def showBarPlot(self, records, minutes):
        self.configureBarPlot(self, minutes)
        plt.bar(records, minutes, align='center', width=0.3)
        plt.show()

    def configureBarPlot(self, minutes):
        mpl.rcParams['toolbar'] = 'none'
        plt.yticks(minutes)
        plt.subplots_adjust(bottom = 0.1, top = 0.95)
        plt.ylabel("Minutes")
        self.addData(self, minutes)