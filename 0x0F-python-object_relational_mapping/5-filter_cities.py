#!/usr/bin/python3
import MySQLdb
import sys

username = "'"+sys.argv[1]+"'"
password = "'"+sys.argv[2]+"'"
database = sys.argv[3]

db = MySQLdb.connect(host='localhost' , user=username, passwd=password, db=database)

cur = db.cursor()

query = "SELECT cities.name FROM cities INNER JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER by cities.id ASC"

cur.execute(query, [sys.argv[4]])

rows = cur.fetchall()
if len(rows) != 0:
    last_value = rows[-1]
    for row in rows:
        print("{}". format(row[0]), end = '')
        if (row != last_value):
            print(', ', end = '')
print()
