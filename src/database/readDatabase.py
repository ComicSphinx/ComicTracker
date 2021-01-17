# @Author: Daniil Maslov
import sqlite3

def main():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM records")
    result = cursor.fetchall()
    print(result)

if __name__ == '__main__':
    main()