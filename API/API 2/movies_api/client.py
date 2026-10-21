from api_client import get_json
import requests

BASE = "http://127.0.0.1:8000"

books = get_json(f"{BASE}/movies")
for book in books:
    print(book)

New_book = {
  "title": "New_book",
  "director": "bob",
  "year": 2000
}
response = requests.post(f"{BASE}/movies", json=New_book, timeout= 5)
print(response.status_code, response.json())

get_json(f"{BASE}/movies/97")