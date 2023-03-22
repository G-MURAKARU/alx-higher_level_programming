#!/usr/bin/python3

"""
    this is the `12-model_state_update_id_2` module.
    this module provides one function, add_state().
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def edit_state(engine) -> None:
    """
    edit_state edits a State entry from a database
    changes the name of state with id of 2 to 'New Mexico'

    Args:
        engine (Engine): SQLAlchemy database engine
    """

    session = Session(bind=engine)

    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"
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

    edit_state(engine)
