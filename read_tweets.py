import json
from unidecode import unidecode

data = []
with open("data.json", "r") as f:
    for line in f:
        tweet = json.loads(line)
        data.append(tweet)

tweet = data[1]

print json.dumps(tweet,indent=4)