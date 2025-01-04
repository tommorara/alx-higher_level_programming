#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


def list_states(username: str, password: str, database: str) -> None:
    """
    Connects to the MySQL server and lists all states
    from the specified database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.

    Returns:
        None
    """
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username,
                             passwd=password, db=database, charset="utf8")
        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER BY id ASC")

        for state in cur.fetchall():
            print(state)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL database: {e}")
    finally:
        if db:
            cur.close()
            db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <username> <password> <database>")
        sys.exit(1)

    list_states(sys.argv[1], sys.argv[2], sys.argv[3])
