#!/usr/bin/python3

"""
    this is the ``0-select_states`` module.
    this module provides one function, func().
"""

import MySQLdb


def select_states(username: str, password: str, db_name: str):
    """
    select_states lists all state entries contained in database `db_name`

    Args:
        username (str): MySQL server username
        password (str): MySQL server password
        db_name (str): MySQL database to query
    """

    with MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=password,
        database=db_name,
    ) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM states ORDER BY id ASC")
            states = cursor.fetchall()

    for state in states:
        print(state)


if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    name, passwd, db = args
    select_states(name, passwd, db)
