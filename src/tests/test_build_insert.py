# @Author: Daniil Maslov (@ComicSphinx)
import sys
sys.path.insert(0, '../database/')
from DatabaseUtilities import DatabaseUtilities as dbu
from datetime import datetime as dt

def test_build_insert():
    record = "test123"
    minutes = 90
    excepted_result = buildString(record, minutes)
    assert(dbu.buildInsert(dbu, record, minutes)) == excepted_result

def buildString(record, minutes):
        tableName = " records "
        insert = "INSERT INTO"+tableName+"VALUES("
        insert += str(dt.now().year)
        insert += "," + str(dt.now().month)
        insert += "," + str(dt.now().day)
        insert += "," + str(minutes)
        insert += ", '" + record + "');"
        return insert