#!/usr/bin/python3

"""A script that lists all cities from the database `hbtn_0e_4_usa`"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    username, password, db, state = sys.argv[1:]

    conn = MySQLdb.connect(
        host="localhost",
        user=username,
        password=password,
        database=db,
        port=3306,
    )

    cursor = conn.cursor()

    # The query is modified to filter the cities by state name
    cursor.execute(
        """
        SELECT cities.name
        FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
        ORDER BY cities.id;
        """,
        (state,),
    )

    results = cursor.fetchall()

    print(", ".join(row[0] for row in results))

    cursor.close()
    conn.close()
