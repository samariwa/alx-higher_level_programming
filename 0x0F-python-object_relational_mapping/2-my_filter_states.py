#!/usr/bin/python3
"""
Displays all values in the states table of the database hbtn_0e_0_usa
whose name matches that supplied as argument.
Usage: ./2-my_filter_states.py <mysql username> \
                                <mysql password> \
                                <database name> \
                                <state name searched>
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

    qry = "SELECT * FROM states WHERE name = '"+sys.argv[4]+"' ORDER by id ASC"

    cur.execute(qry)

    rows = cur.fetchall()
    for row in rows:
        print("({}, '{}')". format(row[0], row[1]))
