# @Author: Daniil Maslov (ComicSphinx)
import sqlite3
from datetime import datetime as dt

tableName = " records "

def main():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(buildInsert("Demo", 60))
    cursor.execute(buildInsert("Demonstration", 120))
    connection.commit()
    connection.close()
    

def buildInsert(string, minutes):
    insert = "INSERT INTO"+tableName+"VALUES("
    insert += str(dt.now().year)
    insert += "," + str(dt.now().month)
    insert += "," + str(dt.now().day)
    insert += "," + str(minutes)
    insert += ", '" + string + "');"
    return insert

if __name__ == '__main__':
    main()