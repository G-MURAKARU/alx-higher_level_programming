#!/usr/bin/python3

"""
    this is the `8-model_state_fetch_first` module.
    this module provides one function, list_first_state().
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def list_first_state(engine) -> None:
    """
    list_states lists all states in a database using ORM

    Args:
        engine: SQLAlchemy database engine
    """

    session = Session(bind=engine)

    state = session.query(State).order_by(State.id).first()

    print(f"{state.id}: {state.name}" if state else "Nothing")

    session.close()


if __name__ == "__main__":
    from sys import argv

    args = argv[1:]
    name, passwd, db = args

    engine = create_engine(
        f"mysql+mysqldb://{name}:{passwd}@localhost/{db}", pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    list_first_state(engine=engine)
