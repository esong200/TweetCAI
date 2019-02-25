import tweepy
from tweepy import OAuthHandler
import os

def authenticate():
    consumer_key = "GG5gDKsljHcSDOHdzbswaCbGS"
    consumer_secret = "BmvMeyadGmFU1N5dhBBqfmEg2SbL6IOB3Eb6jCKtYzO02GtR42"
    access_token = "1092685837668573185-nOznQnUaoxjiHlMZ4y6Jo8CQ7dWsKL"
    access_secret = "5G7JjMFMeEuM8MJzDtQ2dOxu8PLCuhzGIkJFuubeP2hbI"

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth