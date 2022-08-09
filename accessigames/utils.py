import sqlite3 as sql


def database(database, query, params=()):
    result = None
    with sql.connect(database) as connection:
        cursor = connection.cursor()
        result = cursor.execute(query, params)
    return result
