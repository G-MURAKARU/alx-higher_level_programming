#!/usr/bin/python3

"""
    this is the `4-cities_by_state` module.
    this module provides one function, list_cities
"""

import MySQLdb


def list_cities(username: str, password: str, db_name: str) -> None:
    """
    list_cities lists all cities entries from database `db_name`

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
        "SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN \
            states ON cities.state_id = states.id ORDER BY cities.id ASC"
    )
    cities = cur.fetchall()

    for city in cities:
        print(city)

    cur.close()
    conn.close()


if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    name, passwd, db = args
    list_cities(name, passwd, db)
