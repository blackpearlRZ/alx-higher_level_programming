#!/usr/bin/python3
""" Lists all cities from the database """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=username,
                           passwd=password,
                           db=db_name)

    cur = conn.cursor()

    query = 'SELECT cities.id, cities.name, states.name\
            FROM cities \
            LEFT JOIN states \
            ON cities.state_id = states.id'

    cur.execute(query)
    query_result = cur.fetchall()

    for row in query_result:
        print(row)

    cur.close()
    conn.close()
