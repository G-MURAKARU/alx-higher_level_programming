#!/usr/bin/python3

"""
    Start link class to table in database
"""

from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, relationship


def list_cities(engine) -> None:
    """
    list_cities lists all cities in a database

    Args:
        engine (Engine): SQLAlchemy database engine
    """

    session = Session(bind=engine)

    cities = (
        session.query(State, City).filter(City.state_id == State.id).all()
    )

    for city in cities:
        print(f"{city[0].name}: ({city[1].id}) {city[1].name}")

    session.close()


if __name__ == "__main__":
    from sys import argv

    args = argv[1:]
    name, passwd, db = args

    State.cities = relationship(
        "City", order_by=City.id, back_populates="state"
    )

    engine = create_engine(
        f"mysql+mysqldb://{name}:{passwd}@localhost/{db}", pool_pre_ping=True
    )
    # Base.metadata.create_all(engine)

    list_cities(engine)
