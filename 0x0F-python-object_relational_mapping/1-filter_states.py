#!/usr/bin/python3

"""
    this is the ``1-filter_states`` module.
    this module provides one function, filter_states().
"""

import MySQLdb


def filter_states(username: str, password: str, db_name: str) -> None:
    """
    filter_states lists all state entries that begin with 'N' contained in
    database `db_name`

    Args:
        username (str): MySQL server username
        password (str): MySQL server password
        db_name (str): MySQL database to query
    """

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=password,
        database=db_name,
    )
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    )
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    conn.close()


if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    name, passwd, db = args
    filter_states(name, passwd, db)
