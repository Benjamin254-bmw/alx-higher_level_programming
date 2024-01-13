#!/usr/bin/python3
"""takes name of a state as an argument and lists all cities of that state"""
import MySQLdb
import sys

if __name__=="__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELCT cities.name FROM cities INNER JOIN states ON states.id=cities.state_id WHERE states.name=%s", (sys.arv[4], ))
    rows = cur.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    cur.close()
    db.close()
