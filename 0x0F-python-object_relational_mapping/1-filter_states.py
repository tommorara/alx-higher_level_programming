#!/usr/bin/python3

"""A script that lists all states with a name starting with 'N' from
the database `hbtn_0e_0_usa`"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    username, password, db = sys.argv[1:]

    conn = MySQLdb.connect(
        host="localhost",
        user=username,
        password=password,
        database=db,
        port=3306,
    )

    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM states
        WHERE name LIKE BINARY 'N%'
        ORDER BY states.id;
        """
    )

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    conn.close()
