from flask import Blueprint, render_template, jsonify
import requests

main = Blueprint('main', __name__)
pokemon = Blueprint('pokemon', __name__)

@main.route('/')
def hello_world():
    return render_template('index.html')

@pokemon.route('/pokemon/<name>')
def get_pokemon(name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name.lower()}")
    if response.status_code == 200:
        pokemon = response.json()
        data = {
            "name": pokemon['name'],
            "id": pokemon['id'],
            "type": ", ".join([t['type']['name'] for t in pokemon['types']]),
            "height": pokemon['height'],
            "weight": pokemon['weight'],
            "image": pokemon['sprites']['front_default']
        }
        return jsonify(data)
    else:
        return jsonify({"error": "Pokémon not found!"}), 404
