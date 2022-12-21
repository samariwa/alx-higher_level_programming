#!/usr/bin/python3
import MySQLdb
import sys

username = "'"+sys.argv[1]+"'"
password = "'"+sys.argv[2]+"'"
database = sys.argv[3]

db = MySQLdb.connect(host='localhost' , user=username, passwd=password, db=database)

cur = db.cursor()

cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER by id ASC")

rows = cur.fetchall()
for row in rows:
    print("({}, '{}')". format(row[0], row[1]))
