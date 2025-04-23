import json

with open('name.json','r') as file:
    data = json.load(file)
    print(data["name"])