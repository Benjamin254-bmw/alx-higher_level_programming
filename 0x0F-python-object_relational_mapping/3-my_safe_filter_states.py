#!/usr/bin/python3
"""a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument
    script should take 4 arguments:
        mysql username, mysql password, database name and state name
"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8"
        )
    cur = conn.cursor()
    query = """SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"""
    cur.execute(query, (sys.argv[4],))
    query_rows = curr.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
