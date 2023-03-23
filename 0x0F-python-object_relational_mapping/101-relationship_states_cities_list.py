#!/usr/bin/python3

"""
    this is the `101-relationship_states_cities_list` module.
    this module provides one function, list_states().
"""

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def list_states(engine) -> None:
    """
    list_states lists states

    Args:
        engine (Engine): SQLAlchemy database engine
    """

    session = Session(bind=engine)

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")

    session.close()


if __name__ == "__main__":
    from sys import argv

    args = argv[1:]
    name, passwd, db = args

    engine = create_engine(
        f"mysql+mysqldb://{name}:{passwd}@localhost/{db}", pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    list_states(engine)
