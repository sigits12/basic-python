import json
with open('kompasJuli.json', 'r') as f:
    lines = json.loads(f.read())
    for line in lines:
        print(line.get('title'))
        print(line.get('contents'))
