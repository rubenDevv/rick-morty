from flask import jsonfy
import requests
from . import rick_and_mort_bp

def get_characters():
    response = requests.get('https://rickandmortyapi.com/api/character')
    result = jsonfy(response.json)
    return result