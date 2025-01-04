#!/usr/bin/python3

"""A script that lists all cities from the database `hbtn_0e_4_usa`"""

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
        SELECT cities.id, cities.name, states.name
        FROM cities
            JOIN states ON cities.state_id = states.id
        ORDER BY cities.id;
        """
    )

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    conn.close()
