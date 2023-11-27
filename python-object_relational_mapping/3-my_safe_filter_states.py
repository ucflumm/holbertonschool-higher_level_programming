#!/usr/bin/python3
"""
    Once again, write a script that takes in arguments and displays all values
    in the states table of hbtn_0e_0_usa where name matches the argument.
    But this time, write one that is safe from MySQL injections!
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

    cursor.execute("SELECT * FROM states WHERE name LIKE %s\
                    ORDER BY id ASC", (state_name,))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
