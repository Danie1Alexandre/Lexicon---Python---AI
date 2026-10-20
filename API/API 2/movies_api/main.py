from fastapi import FastAPI

app = FastAPI()

movies = [
    {"id": 1, "title": "Toy Story", "director": "John Lasseter", "year": 1995},
    {"id": 2, "title": "Monsters, Inc.", "director": "Pete Docter", "year": 2001},
    {"id": 3, "title": "Finding Nemo", "director": "Andrew Stanton", "year": 2003},
    {"id": 4, "title": "Ratatouille", "director": "Brad Bird", "year": 2007},
]

