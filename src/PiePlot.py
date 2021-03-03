# @Author: Daniil Maslov (ComicSphinx)

import matplotlib as mpl
import matplotlib.pyplot as plt
from Plot import Plot

class PiePlot(Plot):
    
    def showPiePlot(self, records, minutes):
        self.configurePiePlot(self, minutes)
        plt.pie(minutes, labels=records, autopct='%1.0f%%')
        plt.show()

    def configurePiePlot(self, minutes):
        mpl.rcParams['toolbar'] = 'none'
        self.addData(self, minutes)