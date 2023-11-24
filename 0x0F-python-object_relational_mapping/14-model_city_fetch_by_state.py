#!/usr/bin/python3
"""
This script prints all `City` objects from the database `hbtn_0e_14_usa`.

Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.engine.url import URL

from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    username, passw, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    url = {
        "drivername": "mysql+mysqldb",
        "host": "localhost",
        "username": username,
        "password": passw,
        "database": db_name,
    }

    engine = create_engine(URL(**url), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(bind=engine)

    q = session.query(City, State).filter(City.state_id == State.id)

    for city, state in q:
        print(f"{state.name}: ({city.id}) {city.name}")
