# @Author: Daniil Maslov (@ComicSphinx)
from database.DatabaseUtilities import DatabaseUtilities as dbu
from datetime import datetime as dt

class Plot():

    str_sleeping = "Sleeping"
    str_unknown = "?"
    int_maxMinutes = 1440
    int_sleep = 480

    def addData(self, minutes):
        select = dbu.buildSelect(dbu, dt.now().year, dt.now().month, dt.now().day, self.str_sleeping)
        if (dbu.dataIsNotExist(dbu, select)):
            self.addSleep(self)
        
        select = dbu.buildSelect(dbu, dt.now().year, dt.now().month, dt.now().day, self.str_unknown)
        if (dbu.dataIsNotExist(dbu, select)):
            self.addUnknown(self, minutes)

    def addSleep(self):
        insert = dbu.buildInsert(dbu, self.str_sleeping, self.int_sleep)
        dbu.executeCommand(dbu, insert)

    def addUnknown(self, minutes):
        tmp = 0
        for i in range(len(minutes)):
            tmp += minutes[i]
        tmp = self.int_maxMinutes - tmp
        insert = dbu.buildInsert(dbu, self.str_unknown, tmp)
        dbu.executeCommand(dbu, insert)
