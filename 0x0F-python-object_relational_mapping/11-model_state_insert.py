#!/usr/bin/python3

"""
    this is the `11-model_state_insert` module.
    this module provides one function, add_state().
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def add_state(engine) -> None:
    """
    add_state adds a state object to a database

    Args:
        engine (Engine): SQLAlchemy database engine
    """

    session = Session(bind=engine)

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()


if __name__ == "__main__":
    from sys import argv

    args = argv[1:]
    name, passwd, db = args

    engine = create_engine(
        f"mysql+mysqldb://{name}:{passwd}@localhost/{db}", pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    add_state(engine)
