#!/usr/bin/python3
"""
This script lists all values in the `states` table of `hbtn_0e_0_usa`
where `name` matches the argument `state name searched`.

Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
    state name searched (str)
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username, passw, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    searched_name = sys.argv[4]

    db = MySQLdb.connect(user=username, passwd=passw, db=db_name)
    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id".format(
            searched_name
        )
    )
    rows = cur.fetchall()

    for row in rows:
        print(row)
