import json
import requests

url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
r = requests.get(url)
r.raise_for_status()
data = r.json()  # do not create the result file until json is parsed
with open('response.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)
