import requests

def get_json(url):
    response = requests.get(url).json()
    return response