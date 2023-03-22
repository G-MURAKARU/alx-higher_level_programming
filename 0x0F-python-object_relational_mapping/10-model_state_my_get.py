#!/usr/bin/python3

"""
    this is the `10-model_state_my_get` module.
    this module provides one function, get_state().
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def get_state(engine, db_query: str) -> None:
    """
    get_state queries the database for a given state

    Args:
        engine (Engine): SQLAlchemy database engine
    """

    session = Session(bind=engine)

    state = (
        session.query(State)
        .order_by(State.id)
        .filter_by(name=db_query)
        .first()
    )

    print(str(state.id) if state else "Not found")

    session.close()


if __name__ == "__main__":
    from sys import argv

    args = argv[1:]
    name, passwd, db, query = args

    engine = create_engine(
        f"mysql+mysqldb://{name}:{passwd}@localhost/{db}", pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    get_state(engine=engine, db_query=query)
