#!/usr/bin/python3
"""
This script lists all `State` objects that contain
the letter `a` from the database `hbtn_0e_6_usa`.

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

    q = session.query(State).filter(State.name.like("%a%")).order_by(State.id)

    for instance in q:
        print(f"{instance.id}: {instance.name}")
