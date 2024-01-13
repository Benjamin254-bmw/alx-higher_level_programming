#!/usr/bin/python3
"""lists all states from the database hbtn_oe_o_usa"""
import MySQLdb

if __name__=="__main__":
    db = MySQLdb.connect(host="localhost", user=sy.argv[1], passwd=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
