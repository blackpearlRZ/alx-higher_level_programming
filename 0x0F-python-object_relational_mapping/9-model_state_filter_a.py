#!/usr/bin/python3
""" Lists all State objects from the database """

if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    url = 'mysql+mysqldb://\
{}:{}@localhost:3306/{}'.format(username, password, db_name)
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id).all():
        if 'a' in state.name:
            print(f"{state.id}: {state.name}")

    session.close()
