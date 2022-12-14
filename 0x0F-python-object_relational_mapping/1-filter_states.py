#!/usr/bin/python3
"""
 Lists all states with a name starting with N from the database hbtn_0e_0_usa.
 Usage: ./1-filter_states.py <mysql username> \
                             <mysql password> \
                             <database name>
"""
import MySQLdb
import sys


if __name__ == '__main__':
    # establish connection to the database
    username = "'"+sys.argv[1]+"'"
    password = "'"+sys.argv[2]+"'"
    database = sys.argv[3]

    db = MySQLdb.connect(host='localhost',
                         user=username,
                         passwd=password,
                         db=database)

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER by id ASC")

    rows = cur.fetchall()
    for row in rows:
        print("({}, '{}')". format(row[0], row[1]))
