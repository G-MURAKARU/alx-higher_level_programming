#!/usr/bin/python3

"""
    this is the `3-my_safe_filter_states` module.
    this module provides one function, filter_state_safe().
"""

import MySQLdb


def filter_state_safe(
    username: str, password: str, db_name: str, db_query: str
) -> None:
    """
    filter_state_safe finds state entries from `db_name` that match `db_query`
    while avoiding SQL injection

    Args:
        username (str): MySQL server username
        password (str): MySQL server password
        db_name (str): MySQL database to query
        state (str): SQL query parameter
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
        "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC", (db_query,)
    )

    states = cur.fetchall()

    for state in states:
        if state[1] == db_query:
            print(state)

    cur.close()
    conn.close()


if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    name, passwd, db, query = args
    filter_state_safe(name, passwd, db, query)
