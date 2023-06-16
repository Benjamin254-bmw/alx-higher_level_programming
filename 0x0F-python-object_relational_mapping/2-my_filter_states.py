#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the 
states table of hbtn_0e_0_usa where name matches the argument
script should take 4 arguments:
    mysql username, mysql password, database name and state name searched
"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    conn = MySQLdb.connect(
            host="localhost",
            port="3306",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf-8"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'".format(sys.argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == sys.argv[4]:
            print(row)
    cur.close()
    conn.close()
