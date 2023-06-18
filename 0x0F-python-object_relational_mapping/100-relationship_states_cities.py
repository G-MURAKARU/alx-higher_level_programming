#!/usr/bin/python3

"""
    this is the `100-relationship_states_cities` module.
    this module provides one function, add_city_state().
"""

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def add_city_state(engine) -> None:
    """
    list_cities lists all cities in a database

    Args:
        engine (Engine): SQLAlchemy database engine
    """

    session = Session(bind=engine)

    new_state = State(name="California")
    new_city = City(name="San Francisco")

    new_state.cities.append(new_city)

    session.add(new_state)
    session.commit()

    session.close()


if __name__ == "__main__":
    from sys import argv

    args = argv[1:]
    name, passwd, db = args

    engine = create_engine(
        f"mysql+mysqldb://{name}:{passwd}@localhost/{db}", pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    add_city_state(engine)
