#!/usr/bin/python3
"""
This script prints the `State` object in `hbtn_0e_0_usa`
where `name` matches the argument `state name to search`.

Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
    state name to search (str)
"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.engine.url import URL

from model_state import Base, State


if __name__ == "__main__":
    username, passw, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    state_name = sys.argv[4]

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

    q = session.query(State).filter(State.name == state_name)
    q = q.order_by(State.id)

    print(q.first().id) if q.first() else print("Not found")
