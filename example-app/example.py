import requests

def get_random_fact():
    response = requests.get('http://localhost:5001/facts')
    data = response.json()
    return data

def run_app():
    fact = get_random_fact()
    print(fact)

if __name__ == '__main__':
    run_app()

