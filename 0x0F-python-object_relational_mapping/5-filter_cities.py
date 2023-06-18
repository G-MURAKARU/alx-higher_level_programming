#!/usr/bin/python3

"""
    this is the `5-filter_cities` module.
    this module provides one function, filter_cities().
"""

import MySQLdb


def filter_cities(
    username: str, password: str, db_name: str, db_query: str
) -> None:
    """
    filter_cities finds state entries from `db_name` that match `db_query`
    and lists all cities associated with that state

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
        "SELECT cities.name FROM cities INNER JOIN states ON \
            cities.state_id = states.id AND states.name = %s \
                ORDER BY cities.id ASC",
        (db_query,),
    )
    cities = cur.fetchall()

    print(", ".join([city[0] for city in cities]))

    cur.close()
    conn.close()


if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    name, passwd, db, query = args
    filter_cities(name, passwd, db, query)
