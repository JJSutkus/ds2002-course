#!/usr/bin/env python3

import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')

url = f'https://api.github.com/users/{GHUSER}/events'
print(f"Fetching GitHub events from: {url}")

response = requests.get(url)
if response.status_code != 200:
    raise Exception(f"Failed to fetch data: {response.status_code}")

events = json.loads(response.text)

print("\nRecent GitHub activity:\n")
for x in events[:5]:
    event = x['type'] + ' :: ' + x['repo']['name']
    print(event)
