#!/usr/bin/python3
""" Prints the first State object from the database """


if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    user = argv[1]
    passwd = argv[2]
    db_name = argv[3]

    url = "mysql+mysqldb://\
{}:{}@localhost:3306/{}".format(user, passwd, db_name)

    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    session.close()
