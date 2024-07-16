#!/usr/bin/python3
""" Prints the State object with the name passed as argument from the db """

if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    user = argv[1]
    passwd = argv[2]
    db_name = argv[3]
    state_name = argv[4]

    url = f"mysql+mysqldb://{user}:{passwd}@localhost:3306/{db_name}"

    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    session = Session()

    get_state = session.query(State).order_by(State.id).filter(
                State.name == state_name).first()

    if get_state:
        print(get_state.id)
    else:
        print("Not found")

    session.close()
