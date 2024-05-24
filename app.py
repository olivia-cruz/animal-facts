import json
import random
from flask import Flask, jsonify
from flask_cors import CORS

# Creates the Flask app and loads the json file data and returns both
def create_app():
    animal_file = open("animal_facts.json")
    data = json.load(animal_file)
    animal_file.close()
    return Flask(__name__), data

app, animal_facts = create_app()

CORS(app)

# Get all the animal facts
@app.route('/facts', methods=['GET'])
def get_facts():
    return jsonify(animal_facts)

# Get a random animal fact
@app.route('/facts/random', methods=['GET'])
def get_random_fact():
    animal = random.choice(list(animal_facts.keys()))
    fact = animal_facts[animal]
    return jsonify({animal: fact})

# Get a specific animal fact
@app.route('/facts/<animal>', methods=['GET'])
def get_specific_fact(animal):
    if animal.lower() not in list(animal_facts.keys()):
        return "Not Found", 404 
    fact = animal_facts[animal]
    return jsonify({animal: fact})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
