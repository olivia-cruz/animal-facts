import requests

def get_fact():
    response = requests.get('http://localhost:5001/facts/random')
    data = response.json()
    return data

def run_app():
    fact = get_fact()
    print(fact)

if __name__ == '__main__':
    run_app()

