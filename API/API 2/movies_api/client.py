from api_client import get_json
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

URL = "http://127.0.0.1:8000"



New_Movie = {
  "title": "New_Movie",
  "director": "bob",
  "year": 2000
}

get_json(f"{URL}/movies/97")

#with no key
response = requests.post(f"{URL}/movies", json=New_Movie, timeout= 5)
print(response.status_code, response.json())



#using key

response_using_key = requests.post(f"{URL}/movies", json=New_Movie, timeout= 5, headers={"X-API-Key": API_KEY}) 
print("using key")
print(response_using_key.status_code, response_using_key.json())

