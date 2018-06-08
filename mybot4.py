#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Twitter Bot Starter Kit: Bot 4

# This bot tweets out random items from a CSV file

# If you haven't yet created credentials.py, modify credentials.template
# to include your own Twitter account settings. This script will then tweet
# using your bot's account

# Housekeeping: do not edit
import tweepy, time, csv
from random import randint
from credentials import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


# What the bot will tweet
filename = open('az_database_list.csv', 'r')
csv_data = csv.reader(filename)
csv_list = list(csv_data)
filename.close()

# create a continuous loop
while True:

    # select a random item from the csv_list
    random_integer = randint(1, len(csv_list) - 1)
    csv_list_item = csv_list[random_integer]

    # compose the tweet
    tweet = csv_list_item[1] + ' : ' + csv_list_item[2]

    # check to make sure the tweet is not too many characters
    # and if it's too long, shorten it!
    if len(tweet) > 279:
        tweet = tweet[0:276] + '...'

    # post the tweet and print it to the console
    api.update_status(status=tweet)
    print(tweet)

    # wait 10 seconds before repeating
    time.sleep(10)
