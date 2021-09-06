import sqlite3 as sql


def database(database, query, params=()):
    try:
        with sql.connect(database) as con:
            cur = con.cursor()
            if params:
                cur.execute(query, params)
                result = cur.fetchone()
            else:
                cur.execute(query)
                result = cur.fetchone()
    except TypeError as t:
        raise TypeError(t)
    except ConnectionRefusedError as e:
        raise ConnectionRefusedError(e)
    return result
