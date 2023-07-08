import requests
import json

url = "https://akabab.github.io/superhero-api/api/all.json"

resp = requests.get(url)
# print(resp.json)

names_of_characters = ['Hulk', 'Captain America', 'Thanos']
intelligence = {}

for character in resp.json():
    if character['name'] in names_of_characters:
        intelligence[character['powerstats']['intelligence']] = character['name']

# print(intelligence)

sorted_intelligence = dict(sorted(intelligence.items()))
# print(sorted_intelligence)

print(f'Самый умный супергерой: {intelligence[max(intelligence.keys())]}')