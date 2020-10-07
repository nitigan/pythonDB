import requests

BASE = 'http://127.0.0.1:5000/'

responses = requests.get(BASE + 'product')
#print(response.json))

for response in responses :
    print(response.json)