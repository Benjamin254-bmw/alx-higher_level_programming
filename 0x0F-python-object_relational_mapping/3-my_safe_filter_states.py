#!/usr/bin/python3
"""displays values in the table where name matches argument 
& is safe from MySQL injections"""
import MySQLdb
import sys

if __name__=="__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY states.id", (match, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
