#!/usr/bin/python3
"""
This script lists all `cities` from the database `hbtn_0e_4_usa`.

Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username, passw, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(user=username, passwd=passw, db=db_name)
    cur = db.cursor()

    cur.execute(
        "SELECT c.id, c.name, s.name \
        FROM cities c INNER JOIN states s \
        ON c.state_id = s.id \
        ORDER BY c.id"
    )
    rows = cur.fetchall()

    for row in rows:
        print(row)
