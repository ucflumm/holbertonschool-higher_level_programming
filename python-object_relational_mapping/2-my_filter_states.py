#!/usr/bin/python3
"""
    a script that takes in an argument and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state name>"
              .format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:5]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
                    ORDER BY id ASC".format(state_name))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
