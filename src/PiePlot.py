# @Author: Daniil Maslov (ComicSphinx)

from database.DatabaseUtilities import DatabaseUtilities as dbu
import matplotlib as mpl
import matplotlib.pyplot as plt
from datetime import datetime as dt

class PiePlot():
    
    str_sleeping = "Sleeping"
    str_unknown = "?"
    int_maxMinutes = 1440
    int_sleep = 480
    
    def showPiePlot(self, records, minutes):
        self.configurePiePlot(self, minutes)
        plt.pie(minutes, labels=records, autopct='%1.0f%%')
        plt.show()

    def addSleep(self):
        insert = dbu.buildInsert(dbu, self.str_sleeping, self.int_sleep)
        dbu.addDataToDB(dbu, insert)

    def addUnknown(self, minutes):
        tmp = 0
        for i in range(len(minutes)):
            tmp += minutes[i]
        tmp = self.int_maxMinutes - tmp
        insert = dbu.buildInsert(dbu, self.str_unknown, tmp)
        dbu.addDataToDB(dbu, insert)

    def configurePiePlot(self, minutes):
        mpl.rcParams['toolbar'] = 'none'
        select = dbu.buildSelect(dbu, dt.now().year, dt.now().month, dt.now().day, self.str_sleeping)
        if (dbu.dataIsNotExist(dbu, select)):
            self.addSleep(self)
        select = dbu.buildSelect(dbu, dt.now().year, dt.now().month, dt.now().day, self.str_unknown)
        if (dbu.dataIsNotExist(dbu, select)):
            self.addUnknown(self, minutes)
        