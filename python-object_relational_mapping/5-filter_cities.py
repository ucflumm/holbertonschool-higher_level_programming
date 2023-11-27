#!/usr/bin/python3
"""
    Write a script that takes in the name of a state as an argument and lists
    all cities of that state, using the database hbtn_0e_4_usa
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

    cursor.execute("SELECT cities.name FROM cities\
                    INNER JOIN states ON cities.state_id = states.id\
                    WHERE states.name = %s\
                    ORDER BY cities.id ASC", (state_name,))

    rows = cursor.fetchall()

    print(", ".join([row[0] for row in rows]))

    cursor.close()
    db.close()
