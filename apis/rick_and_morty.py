from flask import jsonify, Blueprint
import requests

rick_and_morty_bp = Blueprint('rick_and_morty', __name__)

@rick_and_morty_bp.route("/characters", methods=["GET"])


def get_characters():
    print("Inside /characters route")  # Debugging print
    try:
        response = requests.get('https://rickandmortyapi.com/api/character')
        print(f"Response status code: {response.status_code}")  # Debugging print

        result = response.json()
        character_names = [character['name'] for character in result['results']]
        print(f"Character names: {character_names}")  # Debugging print
        
        return jsonify(character_names)
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({"error": "Failed to fetch characters"}), 500