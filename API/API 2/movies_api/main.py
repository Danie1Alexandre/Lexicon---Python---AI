#444
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

#part 1
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

# Part 3
from dotenv import load_dotenv
import os
from fastapi import Header, Depends

load_dotenv()

API_KEY = os.getenv("API_KEY")

def check_key(x_api_key: str | None = Header(None)):
    
    if not API_KEY:
        raise HTTPException(status_code=500, detail="Server Configuration error")
    
    if x_api_key !=API_KEY:
        raise HTTPException(status_code=401, detail= "not valid API key")


# @app.get("/movies")
# def get_movies():
#     return movies

# @app.get("/movies/{movie_id}")
# def get_movie(movie_id: int):
#     for movie in movies:
#         if movie["id"] == movie_id:
#             return movie
#     raise HTTPException(status_code=404, detail= "Movie Not Found")


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

@app.post("/movies", status_code= 201, dependencies=[Depends(check_key)] )
def create_movie(movie: Movie):
    next_id = max([movie["id"] for movie in movies]) + 1 if movies else 1

    new_movie = movie.model_dump()

    new_movie['id'] = next_id

    movies.append(new_movie)

    return new_movie

# Adding incorrect data will create an error: 422 Invalid data
# you ned to follw the syntax for the bas class.

#1:5

def find_movie(movie_id: int):
    for movie in movies:
        if movie['id'] == movie_id:
            return movie
    raise HTTPException(status_code=404, detail= "Movie Not Found")


@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    return find_movie(movie_id)

@app.put("/movies/{movie_id}", dependencies=[Depends(check_key)])
def update_movie(movie_id: int, updated_movie: Movie):
    movie = find_movie(movie_id)

    movie["title"] = updated_movie.title
    movie["director"] = updated_movie.director
    movie["year"] = updated_movie.year
    return movie


from fastapi import Response 
@app.delete("/movies/{movie_id}", status_code = 204, dependencies=[Depends(check_key)])
def delte_movie(movie_id: int):
    movie = find_movie(movie_id) 

    movies.remove(movie)
    return Response(status_code=204) 
# Response is optional; makes an "empty" return  
# # If you try to delete a movie twice or that  doesn't exist, you get ..
#  "detail": "Movie Not Found" since that is a raised HTTPException from the function (find movie = find_movie(movie_id)) 

# Any change will be deleted when the server is restarted , since we use the computer's " RAM memory" and not a database.

class UpdateMovie(BaseModel):
    title: str | None = None
    director: str | None = None
    year: int | None = None

#part 2

@app.patch("/movies/{movie_id}", dependencies=[Depends(check_key)])
def patch_movie(movie_id: int, updated_movie_data: UpdateMovie):
    movie = find_movie(movie_id)
   
    update = updated_movie_data.model_dump(exclude_unset=True)
    for key, value in update.items():
        movie[key] = value
    
    return movie

#200	Successful Response
# 422	Validation Error
#404 Undocumented Error: Not Found

# Use PATCH when updating One value 
# # Use PUT to replace everything .



