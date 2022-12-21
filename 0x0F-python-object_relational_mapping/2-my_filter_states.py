#!/usr/bin/python3
import MySQLdb
import sys

username = "'"+sys.argv[1]+"'"
password = "'"+sys.argv[2]+"'"
database = sys.argv[3]

db = MySQLdb.connect(host='localhost' , user=username, passwd=password, db=database)

cur = db.cursor()

query = "SELECT * FROM states WHERE name = '"+sys.argv[4]+"' ORDER by id ASC"

cur.execute(query)

rows = cur.fetchall()
for row in rows:
    print("({}, '{}')". format(row[0], row[1]))
