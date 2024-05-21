import requests

def get_random_fact():
    url = 'http://127.0.0.1:5000/fact/random' 
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        animal, fact = list(data.items())[0]
        print(f"Random Animal Fact: {animal} - {fact}")
        
# def get_random_fact():
#     url = '' 
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         animal, fact = list(data.items())[0]
#         print(f"Random Animal Fact: {animal} : {fact}")
#     else:
#         print(f"Failed to get random fact. Status code: {response.status_code}")

if __name__ == "__main__":
    get_random_fact()
