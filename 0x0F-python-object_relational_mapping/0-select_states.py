#!/usr/bin/python3
""" A script that lists all states from database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=mysql_username,
                           passwd=mysql_password,
                           db=database_name,
                           charset="utf8")
    cur = conn.cursor()
    query = "SELECT * FROM states ORDER BY id"
    cur.execute(query)
    query_result = cur.fetchall()

    for row in query_result:
        print(row)

    cur.close()
