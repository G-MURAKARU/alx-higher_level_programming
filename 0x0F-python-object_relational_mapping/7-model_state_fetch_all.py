#!/usr/bin/python3

"""
    this is the `7-model_state_fetch_all` module.
    this module provides one function, list_states().
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def list_states(engine) -> None:
    """
    list_states lists all states in a database using ORM

    Args:
        engine: SQLAlchemy database engine
    """

    session = Session(bind=engine)

    for state in session.query(State).order_by(State.id):
        print(f"{state.id}: {state.name}")

    session.close()


if __name__ == "__main__":
    from sys import argv

    args = argv[1:]
    name, passwd, db = args

    engine = create_engine(
        f"mysql+mysqldb://{name}:{passwd}@localhost/{db}", pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    list_states(engine=engine)
