import tweepy
import os

#Instalattion/Access to Twitter account

auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'],os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_TOKEN_SECRET'])
api = tweepy.API(auth, wait_on_rate_limit = True)

client = tweepy.Client(
    consumer_key = os.environ['CONSUMER_KEY'],
    consumer_secret = os.environ['CONSUMER_SECRET'],
    access_token = os.environ['ACCESS_TOKEN'],
    access_token_secret = os.environ['ACCESS_TOKEN_SECRET']
)


API_KEY = os.environ.get("API_KEY")
