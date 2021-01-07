import sqlite3

def main():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM records")
    results = cursor.fetchall()
    print(results)

if __name__ == '__main__':
    main()