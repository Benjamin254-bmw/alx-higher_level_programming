#!/usr/bin/python3
"""script that takes in the name of a state as an argument
and lists all cities of that
    state, using the database hbtn_0e_4_usa
    Your script should take 4 arguments:
    mysql username, mysql password, database name
    and state name (SQL injection free!)
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
    query = """SELECT name FROM cities
    WHERE state_id = (SELECT id FROM states WHERE name = %s)
    ORDER BY id ASC"""
    cur.execute(query, (sys.argv[4],))
    query_rows = cur.fetchall()

    query_list = []
    for row in query_rows:
        query_list.append(row[0])
    state_str = ", ".join(query_list)
    print(state_str)

    cur.close()
    conn.close()
