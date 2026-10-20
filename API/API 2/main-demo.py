from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# @app.get("/")
# def home():
#     return {"message": "hello world"}

books = [
    {"id": 1, "title": "Dune", "author": "Frank Herbert", "year": 1965},
    {"id": 2, "title": "Neuromancer", "author": "William Gibson", "year": 1984},
    {"id": 3, "title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
    {"id": 4, "title": "Foundation", "author": "Isaac Asimov", "year": 1951},
]



@app.get("/books")
def home():
    return {books}


def find_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code=404, detail= "Book Not Found")

