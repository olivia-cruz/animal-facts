# import json
# import random

# from flask 


# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask, jsonify, render_template, request
import json
import random

app = Flask(__name__)
# animal_facts = []

# def create_app():
#     animal_file = open("animal_facts.json")
#     data = json.load(animal_file)
#     for animal, fact in data.items():
#         animal_facts.append((animal, fact))
#     return Flask(__name__)

# app = create_app()

# @app.route("/facts")
# def generate_fact():
#     animal_fact = animal_facts[random.randint(0, 19)]
#     return f"{animal_fact[0]}: {animal_fact[1]}"

# Load animal facts from the JSON file
with open('animal_facts.json') as f:
    animal_facts = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/facts', methods=['GET'])
def get_facts():
    return jsonify(animal_facts)

@app.route('/fact/random', methods=['GET'])
def get_random_fact():
    animal = random.choice(list(animal_facts.keys()))
    fact = animal_facts[animal]
    return jsonify({animal: fact})

if __name__ == '__main__':
    app.run(debug=True)
