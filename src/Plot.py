from database.DatabaseUtilities import DatabaseUtilities as dbu
import matplotlib.pyplot as plt

class Plot():
    
    def showPlot(self, year, month, day):
        """ Get data from database """
        data = dbu.getDataByYearMonthDay(dbu, year, month, day)
        records,minutes = self.prepareVariablesToPlot(self, data)
        plt.bar(records,minutes)
        plt.show()

    def prepareVariablesToPlot(self, data):
        x = []
        y = []
        for i in range(len(data)):
            """ Append str(record) to X """
            x.append(data[i][4])
            """ Append minutes to Y """
            y.append(data[i][3])
        return x,y