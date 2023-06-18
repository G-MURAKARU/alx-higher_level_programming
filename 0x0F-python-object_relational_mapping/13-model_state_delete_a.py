#!/usr/bin/python3

"""
    this is the `13-model_state_delete_a` module.
    this module provides one function, delete_states().
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def delete_states(engine) -> None:
    """
    delete_states deletes State entries from a database
    deletes all states with letter 'a' in their name

    Args:
        engine (Engine): SQLAlchemy database engine
    """

    session = Session(bind=engine)

    states = (
        session.query(State)
        .filter(State.name.like("%a%"))
        .delete(synchronize_session="fetch")
    )
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

    delete_states(engine)
