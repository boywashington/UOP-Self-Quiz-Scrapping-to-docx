# This code is to learn how to work with JSON file

import json

with open('catalog.json', 'r') as file:
    catalog = json.load(file)

# print(catalog["products"])
for i in catalog["products"]:
    print(i["name"], " is ", i["price"])