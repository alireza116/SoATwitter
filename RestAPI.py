from AppCred import *
from tweepy import OAuthHandler
import tweepy
import json

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)


result = tweepy.Cursor(api.search, q="David Bowie",geocode="40.795895,-73.956880,5mi" )
# result = api.search(q="David Bowie",rpp=100,geocode="41.878114,-87.629798,5mi")
data = []
for tweet in result.items():
    data.append(tweet._json)

print len(data)

for tweet in data:
    print tweet["text"]
    print tweet["geo"]
    print "---------------"

with open("restQuery.json", "w") as outFile:
    outFile.write(json.dumps(data))