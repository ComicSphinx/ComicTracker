from database.DatabaseUtilities import DatabaseUtilities as dbu
import matplotlib as mpl
import matplotlib.pyplot as plt

class Plot():
    
    def showPlot(self, year, month, day):
        """ Get data from database """
        data = dbu.getDataByYearMonthDay(dbu, year, month, day)
        """ Prepare variables to plot """
        records,minutes = self.prepareVariablesToPlot(self, data)
        """ Create plot"""
        self.configurePlot(self, minutes)
        plt.bar(records, minutes, align='center', width=0.3)
        plt.show()

    def configurePlot(self, minutes):
        mpl.rcParams['toolbar'] = 'none'
        plt.yticks(minutes)
        plt.subplots_adjust(bottom = 0.1, top = 0.95)
        plt.ylabel("Minutes")

    def prepareVariablesToPlot(self, data):
        x = []
        y = []
        for i in range(len(data)):
            """ Append str(record) to X """
            x.append(data[i][4])
            """ Append minutes to Y """
            y.append(data[i][3])
        return x,y