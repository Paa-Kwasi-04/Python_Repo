import json
from pathlib import Path

# movies = [
#     {"id": 1, "title": "Terminator", "year": 1989},
#     {"id": 2, "title": "Kindergarten Cop", "year": 1993}
# ]

# data = json.dumps(movies)  # represents dictionary as json data

# print(data)

# Path('movies.json').write_text(data)


# reading from a json file
data = Path('movies.json').read_text()


movies = json.loads(data)
print(movies[0]['title'])
