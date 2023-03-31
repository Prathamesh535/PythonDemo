import requests
import random

randomNumber = random.randint(1,83)
url = "https://swapi.dev/api/people/" + str(randomNumber) 

# A GET request to the API
response = requests.get(url)

response_json = response.json()
print("Name : "+ response_json["name"])
print("Height : "+ response_json["height"])
print("Mass : "+ response_json["mass"])

