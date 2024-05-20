import json
import random

from flask import Flask

animal_facts = []

def create_app():
    animal_file = open("animal_facts.json")
    data = json.load(animal_file)
    for animal, fact in data.items():
        animal_facts.append((animal, fact))
    return Flask(__name__)

app = create_app()

@app.route("/")
def home():
    return "basic flask app"

@app.route("/facts")
def generate_fact():
    animal_fact = animal_facts[random.randint(0, 19)]
    return f"{animal_fact[0]}: {animal_fact[1]}"

if __name__ == "__main__":
    app.run(debug=True)
