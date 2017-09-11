#!/usr/bin/python3

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from pymongo import MongoClient
import json

#keys
consumer_key = "bQjnKowVR7K6Z8zUuLN6IU4rl"
consumer_secret = "24swnGemOmfqDMjtpdnNQaRYpaaU9XYFCRaAUKHx0eKuEKzEhm"

access_token = "899438978625130496-vpxGi7H71MSv81G3TWTdr4mkx44sVMz"
access_token_secret = "EJVEh5vgDvmomVwL4s9Dnp91O4GxOh3GqIMZ0FxmzCO3d"

client = MongoClient('127.0.0.1:27017')
db = client.Main

class MyStreamListener(StreamListener):
    def on_data(self, data):
        print(data)
        insert_item = json.loads(data)
        result = db.tweets.insert_one(insert_item)
        print('Successfully inserted with result: ')
        print(result)


listener = MyStreamListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

stream = Stream(auth, listener)
stream.filter(track=['Toronto'])

