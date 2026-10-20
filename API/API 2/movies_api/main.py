from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

movies = [
    {"id": 1, "title": "Toy Story", "director": "John Lasseter", "year": 1995},
    {"id": 2, "title": "A Bug's Life", "director": "John Lasseter", "year": 1998},
    {"id": 3, "title": "Toy Story 2", "director": "John Lasseter", "year": 1999},
    {"id": 4, "title": "Monsters, Inc.", "director": "Pete Docter", "year": 2001},
    {"id": 5, "title": "Finding Nemo", "director": "Andrew Stanton", "year": 2003},
    {"id": 6, "title": "The Incredibles", "director": "Brad Bird", "year": 2004},
    {"id": 7, "title": "Ratatouille", "director": "Brad Bird", "year": 2007},
    {"id": 8, "title": "WALL-E", "director": "Andrew Stanton", "year": 2008}
]

# @app.get("/movies")
# def get_movies():
#     return movies

@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    raise HTTPException(status_code=404, detail= "Movie Not Found")


@app.get("/movies")
def get_movie(director: str | None = None, year: int | None = None):
    filtered_movies = movies
    if director:
        filtered_movies = [movie for movie in filtered_movies
            if director.lower() in movie["director"].lower()]
              
    if year:
        filtered_movies = [movie for movie in filtered_movies
            if movie["year"]== year]
    
    return filtered_movies

class Movie(BaseModel):
    title: str
    director: str
    year: int

@app.post("/movies", status_code= 201)
def create_movie(movie: Movie):
    next_id = max([movie["id"] for movie in movies]) + 1 if movies else 1

    new_movie = movie.model_dump()

    new_movie['id'] = next_id

    movies.append(new_movie)

    return new_movie

# Adding incorrect data will create an error: 422 Invalid data
# you ned to follw the syntax for the bas class.
        



