#!/usr/bin/env python3

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from datetime import datetime
#from pymongo import MongoClient #For mongo
import pdb
import psycopg2 #postgres
import json

#keys
consumer_key = "bQjnKowVR7K6Z8zUuLN6IU4rl"
consumer_secret = "24swnGemOmfqDMjtpdnNQaRYpaaU9XYFCRaAUKHx0eKuEKzEhm"

access_token = "899438978625130496-vpxGi7H71MSv81G3TWTdr4mkx44sVMz"
access_token_secret = "EJVEh5vgDvmomVwL4s9Dnp91O4GxOh3GqIMZ0FxmzCO3d"

#client = MongoClient('127.0.0.1:27017')
#db = client.Main
conn = psycopg2.connect('dbname=tweets user=mkoo21 password=W9vLXBmlixHWufrx host=martin-election-ward-db.cgdaezyal8oh.us-east-2.rds.amazonaws.com')
#conn = psycopg2.connect('dbname=election_ward user=postgres')
cur = conn.cursor()

def process_tweet(tweet):
    #Parse desired information and insert tweet
    tweet_dict = json.loads(tweet)
    #Check if user exists
    user_dict = tweet_dict['user']
    cur.execute('SELECT * FROM Users WHERE user_id = %s', [user_dict['id']])
    #Insert to user table if user does not exist
    if len(cur.fetchall()) == 0:
        cur.execute('INSERT INTO Users \
                (user_id, \
                user_screen_name, \
                user_location, \
                user_time_zone, \
                user_followers_count, \
                user_status_count) \
                VALUES (%s, %s, %s, %s, %s, %s)', 
                (user_dict['id'], user_dict['screen_name'], user_dict['location'], user_dict['time_zone'], user_dict['followers_count'], user_dict['statuses_count']))

    #Check if retweet
    #if 'retweeted_status' in tweet_dict:
    #Insert tweet
    cur.execute('INSERT INTO Tweets \
            (id,\
            created_at,\
            text,\
            user_id)\
            VALUES (%s, %s, %s, %s)',
            (tweet_dict['id'], datetime.strptime(tweet_dict['created_at'], '%a %b %d %H:%M:%S %z %Y'), tweet_dict['text'], user_dict['id']))

    #Insert hashtags
    #cur.execute('INSERT INTO Hashtags
    #        (text,
    #        tweet_id)
    #        VALUES (%s, %s)',
    #        tweet_dict)
    conn.commit()
    print(tweet_dict['text'])
    print('Successfully inserted tweet')
    
class MyStreamListener(StreamListener):
    def on_data(self, data):
        #insert_item = json.loads(data)
        #result = db.tweets.insert_one(insert_item)
        process_tweet(data)
        print()

listener = MyStreamListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

stream = Stream(auth, listener)
#stream.filter(track=['Toronto'])

stream.filter(track=['anabailaoTO', 'Campbell4Ward4', 'CarmichaelGreb', 'cllrainslie', 'CllrCrawford', 'DenzilMW', 'DoucetteWard13', 'DoucetteWard13', 'FDiGiorgio12', 'FrancesNunziata', 'gordperks', 'hollandmichelle', 'JamesPasternak', 'Janet_Davis', 'JayeRobinson', 'jimkarygiannis', 'joe_cressy', 'joemihevc', 'JohnTory', 'jon_burnside', 'JoshColle', 'JoshMatlow', 'JustinDiCiano', 'kristynwongtam', 'LeeChin8', 'mammolitiward7', 'MariaAugimeri', 'Mark_Grimes', 'mary_margaret32', 'mfragedakis', 'MichaelFordTO', 'm_layton', 'mthompson201', 'NeethanShan', 'norm', 'PaulaFletcher30', 'PerruzzaTO', 'shelleycarroll', 'stephenholyday', 'vcrisanti', 'Ward44_Updates'])

