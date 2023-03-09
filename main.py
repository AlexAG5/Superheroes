import json
import requests
from pprint import pprint
with open("response.json") as f:
    json_data = json.load(f)
def detection(hero_1, hero_2, hero_3):
    all_heroes = {}
    x = 0
    for x in range(len(json_data)):
        hero = json_data[x]["name"]
        if hero == hero_1 or hero == hero_2 or hero == hero_3:
            intelligences = json_data[x]["powerstats"]["intelligence"]
            all_heroes[hero] = intelligences
        x += 1
    max_value = max(all_heroes.values())
    best = {key: values for key, values in all_heroes.items() if values == max_value}
    result = []
    for key, values in best.items():
        result.append(f'Самый умный супергерой это {key}: {values} очков интеллекта.')
    return result

if __name__ == "__main__":
    pprint(detection(hero_1="Hulk", hero_2="Thanos", hero_3="Captain America"))








