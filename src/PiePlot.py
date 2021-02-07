# @Author: Daniil Maslov (ComicSphinx)

from database.DatabaseUtilities import DatabaseUtilities as dbu
import matplotlib as mpl
import matplotlib.pyplot as plt
from datetime import datetime as dt

class PiePlot():
    
    str_sleeping = "Sleeping"
    
    def showPiePlot(self, records, minutes):
        self.configurePiePlot(self)
        plt.pie(minutes, labels=records, autopct='%1.0f%%')
        plt.show()

    def addSleep(self):
        insert = dbu.buildInsert(dbu, self.str_sleeping, 480)
        dbu.addDataToDB(dbu, insert)

    def configurePiePlot(self):
        mpl.rcParams['toolbar'] = 'none'
        if (dbu.dataIsNotExist(dbu, dt.now().year, dt.now().month, dt.now().day, self.str_sleeping)):
            self.addSleep(self)
        