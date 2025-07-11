import sqlite3
import json
from pathlib import Path

# writing to a database

# movies = json.loads(Path('movies.json').read_text())

# with sqlite3.connect('db.sqlite3') as conn:  # returns a connection object
#     command = 'INSERT INTO Movies VALUES(?, ?, ?)'

#     for movie in movies:
#         conn.execute(command, tuple(movie.values()))
#     conn.commit  # for writing to a database


# read from a data base
with sqlite3.connect('db.sqlite3') as conn:  # returns a connection object
    command = 'SELECT * FROM Movies'

    cursor = conn.execute(command)  # return a cursor

    # for row in cursor:
    #     print(row)

    # OR
    movies = cursor.fetchall()
    print(movies)
