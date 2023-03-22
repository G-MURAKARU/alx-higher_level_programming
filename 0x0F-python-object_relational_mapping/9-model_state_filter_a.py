#!/usr/bin/python3

"""
    this is the `9-model_state_filter_a` module.
    this module provides one function, filter_state().
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def filter_state(engine) -> None:
    """
    filter_state lists all states in a database using ORM
    that contain the letter 'a'

    Args:
        engine: SQLAlchemy database engine
    """

    session = Session(bind=engine)

    states = (
        session.query(State)
        .order_by(State.id)
        .filter(State.name.like("%a%"))
        .all()
    )

    for state in states:
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

    filter_state(engine=engine)
